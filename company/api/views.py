import datetime
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from company.api import serializers
from company.models import Company
import json


class CompanyAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        companydata = Company.objects.all().order_by("company_name")
        if companydata:
            return_arr = {'code': 200, 'success': 'true', 'Company': []}
            for detail in companydata:
                array_local = {
                    'id': detail.id or "",
                    'company_name': detail.company_name or "",
                }
                return_arr['Company'].append(array_local)
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 404, 'success': 'false', 'message': 'No Company found'}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.CompanyCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.user.id
            company_instance = Company()
            company_instance.company_name = serializer.data.get("company_name", "")
            # company_instance.u_by =user_id
            # company_instance.is_active = "y"
            # company_instance.is_deleted = "n"
            company_instance.save()

            return_arr = {}
            return_arr['code'] = 200
            return_arr['success'] = 'true'
            return_arr['message'] = 'valid'
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {}
        return_arr['code'] = 602
        return_arr['success'] = 'false'
        return_arr['message'] = 'Error in saving data'
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.CompanyCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            company_name = serializer.validated_data.get("company_name")
            id = serializer.validated_data.get("id")

            company_model = Company.objects.filter(id=id)  # is_deleted="n", is_active='y'

            if not company_model:
                return_arr = {
                    "code": 400,
                    "message": "NO such vehicle found",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            company_model = company_model.first()
            if company_name:
                company_model.vehicle_name = company_name

            save_object = company_model.save()

            if save_object is None:
                return_arr = {"code": 200,"message": "Comapny Update successfully","success": True,}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = { "code": 400,"message": "Error in saving","success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in posting", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

