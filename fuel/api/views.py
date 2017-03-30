from django.core.paginator import EmptyPage, Paginator
import json
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from fuel.api import serializers
from fuel.models import Fuel


class FuleAPIView(APIView):
    permission_classes = [AllowAny]
    instance_fields = ['vehicle_id', 'fuel_date', 'odometer_id', 'fuel_measure', 'fuel_price', 'currency', 'fuel_type',
                       'vendor_name', 'comment']

    def get(self, request, format=None):
        serializer = serializers.FuelReadSerializer
        fuledata = Fuel.objects.filter(is_deleted=False).order_by('-modified').extra(
            select={
                "vehicle_name": "SELECT vehicle_name from vehicle_vehicle WHERE vehicle_vehicle.id=fuel_fuel.vehicle_id LIMIT 1",
            }
        );

        paginator = Paginator(fuledata, 5)
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
                'pages': paginator.num_pages, 'next_page_number': next_page_number, 'total': fuledata.count(),
                'previous_page_number': previous_page_number,
                'success': 'true', 'Fuel': serializer.data
            }
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        else:
            return_arr = {'code': 200, 'success': 'false', 'message': 'No Fuel found', 'Fuel': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.FuelCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            fuel_instance = Fuel()
            for instance_field in self.instance_fields:
                fuel_instance.__setattr__(instance_field, serializer.data.get(instance_field))

            fuel_instance.i_by = request.user.id
            fuel_instance.u_by = request.user.id
            fuel_instance.save()

            return_arr = {"code": 200, "success": True, "messages": "valid"}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 602, "success": False, "messages": "Error in Posting data"}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.FuelCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            fuel_model = Fuel.objects.filter(id=serializer.validated_data.get("id"))  # is_deleted="n", is_active='y'

            if not fuel_model:
                return_arr = {"code": 400, "success": False, "messages": "No Such Fuel Found"}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

                fuel_model = fuel_model.first()
            for instance_field in self.instance_fields:
                if (serializer.data.get(instance_field)):
                    fuel_model.__setattr__(instance_field, serializer.data.get(instance_field))

            if serializer.validated_data.get("is_deleted"):
                fuel_model.is_deleted = True
            fuel_model.u_by = request.user.id
            save_object = fuel_model.save()

            if save_object is None:
                return_arr = {"code": 200, "message": "Fuel Update successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in Postingss", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
