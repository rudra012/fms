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
                       'job_nbr',  # 'job_status'
                       ]

    def get(self, request, format=None):
        serializer = serializers.JobReadSerializer

        if (request.GET.get('id')):
            jobdata = Job.objects.filter(is_deleted=False, id=request.GET.get('id')).order_by('-modified').extra(
                select={
                    "user_first_name": "SELECT first_name from users_user WHERE users_user.id=jobs_job.user_id LIMIT 1",
                    "vehicle_name": "SELECT vehicle_name from vehicle_vehicle WHERE vehicle_vehicle.id=jobs_job.vehicle_id LIMIT 1",
                }
            );
        else:
            jobdata = Job.objects.filter(is_deleted=False).order_by('-modified').extra(
                select={
                    "user_first_name": "SELECT first_name from users_user WHERE users_user.id=jobs_job.user_id LIMIT 1",
                    "vehicle_name": "SELECT vehicle_name from vehicle_vehicle WHERE vehicle_vehicle.id=jobs_job.vehicle_id LIMIT 1",
                }
            );

        paginator = Paginator(jobdata, 5)
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
            return_arr = {'code': 200, 'has_next': contacts.has_next(), 'has_previous': contacts.has_previous(),
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
            job_instance = Job()
            for instance_field in self.instance_fields:
                job_instance.__setattr__(instance_field, serializer.data.get(instance_field))

            if (job_instance.user_id):
                job_instance.job_status = 'a'
            else:
                job_instance.job_status = 'p'

            job_instance.i_by = request.user.id
            job_instance.u_by = request.user.id
            job_instance.save()

            return_arr = {"code": 200, "success": True, "messages": "valid"}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 602, "success": False, "messages": "Error in Posting data"}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.JobCreateUpdateSerializer(data=request.data, context={"request": request})
        print (serializer.is_valid())
        if serializer.is_valid():
            job_model = Job.objects.filter(id=serializer.validated_data.get("id"))  # is_deleted="n", is_active='y'
            if not job_model:
                return_arr = {"code": 400, "success": False, "messages": "No Such Job Found"}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            job_model = job_model.first()
            for instance_field in self.instance_fields:
                if (serializer.data.get(instance_field)):
                    job_model.__setattr__(instance_field, serializer.data.get(instance_field))

            if (job_model.user_id):
                job_model.job_status = 'a'
            else:
                job_model.job_status = 'p'

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
