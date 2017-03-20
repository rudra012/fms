import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from jobs.api import serializers
from jobs.models import Job




class JobAPIView(APIView):
    permission_classes = [AllowAny]
    instance_fields = ['user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
                       # 'job_status'
                       ]

    def get(self, request, format=None):
        serializer = serializers.JobReadSerializer
        # groupdata = Job.objects.filter(is_deleted=False).extra(
        #     select={
        #         "company_name": "SELECT company_name from company_company WHERE company_company.id=group_group.company_id LIMIT 1",
        #     },
        # ).order_by('-modified')

        jobdata = Job.objects.filter(is_deleted=False).order_by('-modified')

        paginator = Paginator(jobdata, 1)
        page = request.GET.get('page')

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        previous_page_number = 1
        if contacts.has_previous():
            previous_page_number = contacts.previous_page_number()
        next_page_number = 1
        if (contacts.has_next()):
            next_page_number = contacts.next_page_number()

        if contacts:
            serializer = serializer(contacts, many=True)
            return_arr = {
                'code': 200, 'has_next': contacts.has_next(), 'has_previous': contacts.has_previous(),
                'pages': paginator.num_pages, 'next_page_number': next_page_number, 'total': jobdata.count(),
                'previous_page_number': previous_page_number,
                'success': 'true', 'Job': serializer.data
            }
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        else:
            return_arr = {'code': 200, 'success': 'false', 'message': 'No Group found', 'Job': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.JobCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            group_instance = Job()
            for instance_field in self.instance_fields:
                group_instance.__setattr__(instance_field, serializer.data.get(instance_field))

            group_instance.i_by = request.user.id
            group_instance.u_by = request.user.id
            group_instance.save()
            return_arr = {"code": 200, "success": True, "messages": "valid"}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 602, "success": False, "messages": "Error in Posting data"}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.JobCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            job_model = Job.objects.filter(id=serializer.validated_data.get("id"))  # is_deleted="n", is_active='y'
            if not job_model:
                return_arr = {"code": 400, "success": False, "messages": "No Such Job Found"}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            job_model = job_model.first()
            for instance_field in self.instance_fields:
                if (serializer.data.get(instance_field)):
                    job_model.__setattr__(instance_field, serializer.data.get(instance_field))

            if serializer.validated_data.get("is_deleted"):
                job_model.is_deleted = True
                job_model.u_by = request.user.id
            save_object = job_model.save()

            if save_object is None:
                return_arr = {"code": 200, "message": "Job Update successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in Postings", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
