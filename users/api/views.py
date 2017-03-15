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


class UserAPIView(APIView):
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user_list = User.objects.filter(is_deleted=False).exclude(id=request.user.id).order_by('-modified')
        serializer = self.serializer_class(user_list, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        data = request.data
        get_deal = User.objects.get(pk=request.data.get('id'))
        serializer = self.serializer_class(get_deal, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        data = request.data
        delete_currency = User.objects.filter(pk=request.data.get('id')).update(is_deleted=True)
        response_arr = {"success": "true"}
        return Response(response_arr, status=HTTP_200_OK)
