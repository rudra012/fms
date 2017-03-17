import json
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse

from base.constant import vehicle_status
from vehicle.api import serializers
from vehicle.models import Vehicle


class VehicleStatusAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return_arr = {'code': 200, 'success': 'true', 'message': 'vehicle_status', 'vehicle_status': vehicle_status}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])





class VehicleListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        if (request.GET.get('id')):
            vehicledata = Vehicle.objects.filter(is_deleted=False, id=request.GET.get('id')).order_by('-modified')
        else:
            vehicledata = Vehicle.objects.filter(is_deleted=False, i_by=request.user.id).order_by('-modified')

        if vehicledata:
            return_arr = {'code': 200, 'success': 'true', 'Vehicle': []}
            for detail in vehicledata:
                array_local = {
                    'id': detail.id or "",
                    'vehicle_name': detail.vehicle_name or "",
                    'vin_no': detail.vin_no or "",
                    'vehicle_make': detail.vehicle_make or "",
                    'vehicle_model': detail.vehicle_model or "",
                    'vehicle_year': detail.vehicle_year or "",
                    'vehicle_license': detail.vehicle_license or "",
                    'registration_state': detail.registration_state or "",
                    'vehiclestatus_id': detail.vehiclestatus_id or "",
                    'group_id': detail.group_id or "",
                    'contact_id': detail.contact_id or "",
                    'ownership': detail.ownership or "",
                    'company_id ': detail.company_id or "",
                    'i_by ': detail.i_by or "",
                    'u_by ': detail.u_by or "",
                    'vehicle_status':vehicle_status
                }
                return_arr['Vehicle'].append(array_local)
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 200, 'success': 'true', 'message': 'No Vehicle found', 'Vehicle': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.VehiclCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            vehicle_instance = Vehicle()
            vehicle_instance.vehicle_name = serializer.data.get("vehicle_name", "")
            vehicle_instance.vehicle_make = serializer.data.get("vehicle_make", "")
            vehicle_instance.vehicle_model = serializer.data.get("vehicle_model", "")
            vehicle_instance.vehicle_year = serializer.data.get("vehicle_year", "")
            vehicle_instance.vehicle_license = serializer.data.get("vehicle_license", "")
            vehicle_instance.registration_state = serializer.data.get("registration_state", "")
            vehicle_instance.vin_no = serializer.data.get("vin_no", "")
            vehicle_instance.vehiclestatus_id = serializer.data.get("vehiclestatus_id", "")
            vehicle_instance.group_id = serializer.data.get("group_id", "")
            vehicle_instance.contact_id = serializer.data.get("contact_id", "")
            vehicle_instance.ownership = serializer.data.get("ownership", "")
            vehicle_instance.u_by = request.user.id or ""
            vehicle_instance.i_by = request.user.id or ""
            vehicle_instance.save()

            return_arr = {}
            return_arr['code'] = 200
            return_arr['success'] = 'true'
            return_arr['message'] = 'Vehicle Add Successfully'
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {}
        return_arr['code'] = 602
        return_arr['success'] = 'false'
        return_arr['message'] = 'Error in saving data'
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.VehiclCreateUpdateSerializer(data=request.data, context={"request": request})
        print (request.data.get('is_deleted'))
        if serializer.is_valid():
            id = serializer.validated_data.get("id")
            vehicl_model = Vehicle.objects.filter(id=id)  # is_deleted="n", is_active='y'

            if not vehicl_model:
                return_arr = {
                    "code": 400,
                    "message": "NO such vehicle found",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            vehicl_model = vehicl_model.first()
            if serializer.validated_data.get("vehicle_name"):
                vehicl_model.vehicle_name = serializer.validated_data.get("vehicle_name")


            if serializer.validated_data.get("vin_no"):
                vehicl_model.vin_no = serializer.validated_data.get("vin_no")

            if serializer.validated_data.get("vehiclestatus_id"):
                vehicl_model.vehiclestatus_id = serializer.validated_data.get("vehiclestatus_id")

            if serializer.validated_data.get("group_id"):
                vehicl_model.group_id = serializer.validated_data.get("group_id")

            if serializer.validated_data.get("contact_id"):
                vehicl_model.group_id = serializer.validated_data.get("contact_id")

            if serializer.validated_data.get("vehicle_make"):
                vehicl_model.vehicle_make = serializer.validated_data.get("vehicle_make")

            if serializer.validated_data.get("vehicle_model"):
                vehicl_model.vehicle_model = serializer.validated_data.get("vehicle_model")

            if serializer.validated_data.get("vehicle_year"):
                vehicl_model.vehicle_year = serializer.validated_data.get("vehicle_year")

            if serializer.validated_data.get("vehicle_license"):
                vehicl_model.vehicle_license = serializer.validated_data.get("vehicle_license")

            if serializer.validated_data.get("registration_state"):
                vehicl_model.registration_state = serializer.validated_data.get("registration_state")


            if serializer.validated_data.get("ownership"):
                vehicl_model.ownership = serializer.validated_data.get("ownership")

            if serializer.validated_data.get("company_id"):
                vehicl_model.company_id = serializer.validated_data.get("company_id")


            if serializer.validated_data.get("is_deleted"):
                vehicl_model.is_deleted = True

            save_object = vehicl_model.save()

            if save_object is None:
                return_arr = {"code": 200, "message": "Vehicle edited successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in posting", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
