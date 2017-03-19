from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
import json

from serializers import UserLoginSerializer, UserCreateSerializer
from users.api import serializers
from users.models import User

from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import HttpResponse


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class UserAPIView(APIView):
#     serializer_class = UserCreateUpdateSerializer
#     permission_classes = [AllowAny]
#
#     def get(self, request, *args, **kwargs):
#         user_list = User.objects.filter(is_deleted=False).exclude(id=request.user.id).order_by('-modified')
#         serializer = self.serializer_class(user_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#
#     def put(self, request, *args, **kwargs):
#         data = request.data
#         get_deal = User.objects.get(pk=request.data.get('id'))
#         serializer = self.serializer_class(get_deal, data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         data = request.data
#         delete_currency = User.objects.filter(pk=request.data.get('id')).update(is_deleted=True)
#         response_arr = {"success": "true"}
#         return Response(response_arr, status=HTTP_200_OK)


class UserAPIView(APIView):
    permission_classes = [AllowAny]
    instance_fields = [
        # 'password',
        'first_name', 'last_name', 'mobile_no', 'user_type', 'group_id', 'company_id', 'address', 'state_name',
        'city_name', 'postal_code', 'country_id', 'employee_no', 'job_title', 'contact_person', 'website_url',
        'contact_person_email', 'contact_person_phone', 'license_no', 'license_region',  # 'start_date','leave_date'
    ]

    def get(self, request, format=None):
        serializer = serializers.UserGetUpdateSerializer

        if (request.GET.get('id')):
            userdata = User.objects.filter(is_deleted=False, id=request.GET.get('id')).order_by('-modified')
        else:
            userdata = User.objects.filter(is_deleted=False, i_by=request.user.id).order_by('-modified').exclude(
                id=request.user.id)
            if request.GET.get('type') == 'v':
                userdata = userdata.filter(user_type='v')
                # else:
                #     userdata = userdata.filter(user_type='u')

        if userdata:
            serializer = serializer(userdata, many=True)
            return_arr = {'code': 200, 'success': 'true', 'User': serializer.data}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 200, 'success': 'false', 'message': 'No User found', 'User': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.UserCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():

            if (serializer.data.get("email")):
                check_obj = User.objects.filter(email=serializer.data.get("email"))
                if check_obj:
                    return_arr = {"code": 600, "success": False, "message": "Email Already In use."}
                    return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            check_obj = User.objects.filter(username=serializer.data.get("username"))
            if check_obj:
                return_arr = {"code": 600, "success": False, "message": "Username Already Taken."}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_obj = User(
                username=serializer.data.get("username", ""),
                email=serializer.data.get("email", ""),
            )
            user_obj.set_password(serializer.data.get("password"))

            for instance_field in self.instance_fields:
                user_obj.__setattr__(instance_field, serializer.data.get(instance_field, ""))

            user_obj.i_by = request.user.id
            user_obj.u_by = request.user.id
            user_obj.save()

            return_arr = {"code": 200, "success": True, "message": "User Add Success Fully."}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {"code": 602, "success": False, "message": "Error in Posting data."}
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        serializer = serializers.UserCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            if not serializer.validated_data.get("id"):
                return_arr = {"code": 602, "success": False, "message": "No Contact found."}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_model = User.objects.filter(id=serializer.validated_data.get("id"))

            if not user_model:
                return_arr = {"code": 400, "success": False, "message": "NO such User found."}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_model = user_model.first()
            if (serializer.validated_data.get("email")):
                check_user = User.objects.filter(email=serializer.validated_data.get("email")).exclude(id=id)
                if check_user:
                    return_arr = {"code": 400, "success": False, "message": "Email already in use."}
                    return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            check_user = User.objects.filter(username=serializer.validated_data.get("username")).exclude(id=id)
            if check_user:
                return_arr = {"code": 400, "success": False, "message": "Username already in use."}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            for instance_field in self.instance_fields:
                if serializer.validated_data.get(instance_field):
                    user_model.__setattr__(instance_field, serializer.data.get(instance_field, ""))

            if serializer.validated_data.get("username"):
                user_model.username = serializer.validated_data.get("username")

            if serializer.validated_data.get("email"):
                user_model.email = serializer.validated_data.get("email")

            if serializer.validated_data.get("is_deleted"):
                user_model.is_deleted = True

            # if serializer.validated_data.get("start_date"):
            #     user_model.start_date = serializer.validated_data.get("start_date")
            # if serializer.validated_data.get("leave_date"):
            #     user_model.leave_date = serializer.validated_data.get("leave_date")

            user_model.u_by = request.user.id
            if user_model.save() is None:
                return_arr = {"code": 200, "message": "Contact Update successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in Postingss", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
