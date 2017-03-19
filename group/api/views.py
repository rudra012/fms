import datetime
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from group.api import serializers
from group.models import Group


class GroupAPIView(APIView):
    permission_classes = [AllowAny]
    instance_fields = ['company_id', 'group_name']

    def get(self, request, format=None):
        groupdata = Group.objects.filter(is_deleted=False).extra(
            select={
                "company_name": "SELECT company_name from company_company WHERE company_company.id=group_group.company_id LIMIT 1",
            },
        ).order_by('-modified')

        if groupdata:
            return_arr = {'code': 200, 'success': 'true', 'Group': []}
            for detail in groupdata:
                array_local = {
                    'id': detail.id or "",
                    'group_name': detail.group_name or "",
                    'company_id': detail.company_id or "",
                    'company_name': detail.company_name or "",
                }
                return_arr['Group'].append(array_local)
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 200, 'success': 'false', 'message': 'No Group found', 'Group': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.GroupCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            group_instance = Group()
            for instance_field in self.instance_fields:
                group_instance.__setattr__(instance_field, serializer.data.get(instance_field))

            group_instance.i_by = request.user.id
            group_instance.u_by = request.user.id
            group_instance.save()

            return_arr = {}
            return_arr['code'] = 200
            return_arr['success'] = 'true'
            return_arr['message'] = 'valid'
            return_arr['Group'] = {
                'id': group_instance.id or "",
                'group_name': group_instance.group_name or "",
                'company_id': group_instance.company_id or "",
            }

            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 602, "success": False, "messages": "Error in Posting data"}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.GroupCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            group_model = Group.objects.filter(id=serializer.validated_data.get("id"))  # is_deleted="n", is_active='y'

            if not group_model:
                return_arr = {"code": 400, "success": False, "messages": "No Such Group Found"}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            group_model = group_model.first()
            for instance_field in self.instance_fields:
                if (serializer.data.get(instance_field)):
                    group_model.__setattr__(instance_field, serializer.data.get(instance_field))

            if serializer.validated_data.get("is_deleted"):
                group_model.is_deleted = True
            group_model.u_by = request.user.id
            save_object = group_model.save()

            if save_object is None:
                return_arr = {"code": 200, "message": "Group Update successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in Postingss", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
