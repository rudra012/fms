import json
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse

from vehicle.api import serializers
from vehicle.models import Vehicle


class VehicleListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        vehicledata = Vehicle.objects.all().order_by("vehicle_name")
        if vehicledata:
            return_arr = {'code': 200, 'success': 'true', 'Vehicle': []}
            for detail in vehicledata:
                # TODOne: add this to admin panel
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
                }
                return_arr['Vehicle'].append(array_local)
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 404, 'success': 'false', 'message': 'No Vehicle found'}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])


    def post(self, request, format=None):
        serializer = serializers.VehiclCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.user.id
            vehicle_instance = Vehicle()
            vehicle_instance.vehicle_name = serializer.data.get("vehicle_name", "")
            # vehicle_instance.u_by =user_id
            # vehicle_instance.is_active = "y"
            # vehicle_instance.is_deleted = "n"
            vehicle_instance.save()

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
        serializer = serializers.UpdateVehicleSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            vehicle_name = serializer.validated_data.get("vehicle_name")
            id = serializer.validated_data.get("id")
            vehicl_model = Vehicle.objects.filter(id=id).order_by('-modified')  # is_deleted="n", is_active='y'

            if not vehicl_model:
                return_arr = {
                    "code": 400,
                    "message": "NO such vehicle found",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            vehicl_model = vehicl_model.first()
            if vehicle_name:
                vehicl_model.vehicle_name = vehicle_name

            save_object = vehicl_model.save()

            if save_object is None:
                return_arr = {"code": 200,"message": "Vehicle edited successfully","success": True,}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = { "code": 400,"message": "Error in saving","success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in posting", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

