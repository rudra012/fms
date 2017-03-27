import json

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger, Paginator
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
    instance_fields = [
        'vehicle_name', 'vehicle_make', 'vehicle_model', 'vehicle_year', 'vehicle_license', 'registration_state',
        'vin_no', 'vehiclestatus_id', 'group_id', 'contact_id', 'ownership'
    ]

    def get(self, request, format=None):
        serializer = serializers.VehiclReadSerializer

        if (request.GET.get('id')):
            vehicledata = Vehicle.objects.filter(is_deleted=False, id=request.GET.get('id')).order_by('-modified')
        else:
            vehicledata = Vehicle.objects.filter(is_deleted=False, i_by=request.user.id).order_by('-modified')

        paginator = Paginator(vehicledata, 5)
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

        if vehicledata:
            serializer = serializer(contacts, many=True)
            return_arr = {
                'code': 200, 'has_next': contacts.has_next(), 'has_previous': contacts.has_previous(),
                'pages': paginator.num_pages, 'next_page_number': next_page_number, 'total': vehicledata.count(),
                'previous_page_number': previous_page_number,
                'success': 'true', 'Vehicle': serializer.data
            }
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        else:
            return_arr = {'code': 200, 'success': 'true', 'message': 'No Vehicle found', 'Vehicle': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.VehiclCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            vehicle_instance = Vehicle()
            for instance_field in self.instance_fields:
                vehicle_instance.__setattr__(instance_field, serializer.data.get(instance_field, ""))

            vehicle_instance.u_by = request.user.id or ""
            vehicle_instance.i_by = request.user.id or ""
            vehicle_instance.save()

            return_arr = {"code": 200, "message": "Vehicle Add Successfully", "success": True}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 400, "message": "Error in saving data", "success": False}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.VehiclCreateUpdateSerializer(data=request.data, context={"request": request})
        print (request.data.get('is_deleted'))
        if serializer.is_valid():
            id = serializer.validated_data.get("id")
            vehicl_model = Vehicle.objects.filter(id=id)  # is_deleted="n", is_active='y'

            if not vehicl_model:
                return_arr = {"code": 400, "message": "NO such vehicle found", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            vehicl_model = vehicl_model.first()
            for instance_field in self.instance_fields:
                if serializer.validated_data.get(instance_field):
                    vehicl_model.__setattr__(instance_field, serializer.data.get(instance_field, ""))

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
