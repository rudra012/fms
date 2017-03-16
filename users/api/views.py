from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
import json
from serializers import UserCreateSerializer, UserCreateUpdateSerializer

from serializers import UserLoginSerializer
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

    def get(self, request, format=None):
        if (request.GET.get('id')):
            userdata = User.objects.filter(is_deleted=False, id=request.GET.get('id')).order_by('-modified')
        else:
            userdata = User.objects.filter(is_deleted=False).order_by('-modified').exclude(id=request.user.id)

        if userdata:
            return_arr = {'code': 200, 'success': 'true', 'User': []}
            for detail in userdata:
                array_local = {
                    'id': detail.id or "",
                    'username': detail.username or "",
                    'password': detail.password or "",
                    'email': detail.email or "",
                    'first_name': detail.first_name or "",
                    'last_name': detail.last_name or "",
                    'group_id': detail.group_id or "",
                    'mobile_no': detail.mobile_no or "",
                    'address': detail.address or "",
                    'city_name': detail.city_name or "",
                    'state_name': detail.state_name or "",
                    'postal_code': detail.postal_code or "",
                    'country_id': detail.country_id or "",
                    'employee_no': detail.employee_no or "",
                    'start_date': detail.start_date or "",
                    'leave_date': detail.leave_date or "",
                    'user_type': detail.user_type or "",
                    'license_no': detail.license_no or "",
                    'license_region': detail.license_region or "",
                    'company_id': detail.company_id or "",
                }
                return_arr['User'].append(array_local)
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {'code': 200, 'success': 'false', 'message': 'No User found', 'Group': []}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def post(self, request, format=None):
        serializer = serializers.UserCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():

            check_obj = User.objects.filter(email=serializer.data.get("email"))
            if check_obj:
                return_arr = {}
                return_arr['code'] = 600
                return_arr['success'] = 'false'
                return_arr['message'] = 'Email Already In use.'
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            check_obj = User.objects.filter(username=serializer.data.get("username"))
            if check_obj:
                return_arr = {}
                return_arr['code'] = 600
                return_arr['success'] = 'false'
                return_arr['message'] = 'Username Already Taken.'
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_obj = User(
                username=serializer.data.get("username", ""),
                email=serializer.data.get("email", ""),
            )
            user_obj.set_password(serializer.data.get("password", ""))
            user_obj.i_by = request.user.id
            user_obj.u_by = request.user.id
            user_obj.first_name = serializer.data.get("first_name", "")
            user_obj.last_name = serializer.data.get("last_name", "")
            user_obj.group_id = serializer.data.get("group_id", "")
            user_obj.company_id = serializer.data.get("company_id", "")
            user_obj.save()

            return_arr = {}
            return_arr['code'] = 200
            return_arr['success'] = 'true'
            return_arr['message'] = 'Contact Add Success fully'
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

        return_arr = {}
        return_arr['code'] = 602
        return_arr['success'] = 'false'
        return_arr['message'] = 'Error in Posting data'
        return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

    def put(self, request, *args, **kwargs):
        print (request.data)
        serializer = serializers.UserCreateUpdateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():

            id = serializer.validated_data.get("id")
            if not id:
                return_arr = {}
                return_arr['code'] = 602
                return_arr['success'] = 'false'
                return_arr['message'] = 'No Contact found'
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_model = User.objects.filter(id=id)

            if not user_model:
                return_arr = {
                    "code": 400,
                    "message": "NO such User found",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            user_model = user_model.first()

            check_user = User.objects.filter(email=serializer.validated_data.get("email")).exclude(id=id)
            if check_user:
                return_arr = {
                    "code": 400,
                    "message": "Email already in use",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            check_user = User.objects.filter(username=serializer.validated_data.get("username")).exclude(id=id)
            if check_user:
                return_arr = {
                    "code": 400,
                    "message": "Username already in use",
                    "success": False
                }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])

            if serializer.validated_data.get("username"):
                user_model.username = serializer.validated_data.get("username")
            if serializer.validated_data.get("group_id"):
                user_model.group_id = serializer.validated_data.get("group_id")
            if serializer.validated_data.get("is_deleted"):
                user_model.group_id = True

            if serializer.validated_data.get("first_name"):
                user_model.first_name = serializer.validated_data.get("first_name")

            if serializer.validated_data.get("last_name"):
                user_model.last_name = serializer.validated_data.get("last_name")

            if serializer.validated_data.get("mobile_no"):
                user_model.mobile_no = serializer.validated_data.get("mobile_no")

            user_model.u_by = request.user.id
            save_object = user_model.save()

            if save_object is None:
                return_arr = {"code": 200, "message": "Contact Update successfully", "success": True, }
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
            else:
                return_arr = {"code": 400, "message": "Error in saving", "success": False}
                return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
        else:
            return_arr = {"code": 400, "message": "Error in Postingss", "success": False}
            return HttpResponse(json.dumps(return_arr), status=return_arr['code'])
