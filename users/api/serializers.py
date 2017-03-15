import datetime
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
    Serializer
)
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers

from base.utils import CustomValidation

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address', write_only=True)
    email2 = EmailField(label='Confirm Email', write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'token',
            'email',
            'email2',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.last_login = datetime.datetime.now()
        user_obj.save()
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        user_a = User.objects.filter(username__iexact=username)
        user_b = User.objects.filter(email__iexact=username)
        user_qs = (user_a | user_b).distinct()
        if user_qs.exists() and user_qs.count() == 1:
            user_obj = user_qs.first()
            password_passes = user_obj.check_password(password)
            user_obj.last_login = datetime.datetime.now()
            if not user_obj.is_active:
                raise ValidationError("This user is inactive")
            if password_passes:
                data['username'] = user_obj.username
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                data['token'] = token
                return data
        raise ValidationError("Invalid credentials")


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = CharField(allow_blank=True, required=False, allow_null=True)
    username = CharField(allow_blank=True, required=False, allow_null=True)
    email = CharField(allow_blank=True, required=False, allow_null=True)

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email') or ""
        password = validated_data['password']
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.first_name = validated_data.get('first_name') or ""
        user_obj.group_id = validated_data.get('group_id')
        user_obj.mobile_no = validated_data.get('mobile_no')
        user_obj.address = validated_data.get('address')
        user_obj.city_name = validated_data.get('city_name')
        user_obj.state_name = validated_data.get('state_name')
        user_obj.postal_code = validated_data.get('postal_code')
        user_obj.country_id = validated_data.get('country_id')
        user_obj.employee_no = validated_data.get('employee_no')
        user_obj.job_title = validated_data.get('job_title')
        user_obj.start_date = validated_data.get('start_date')
        user_obj.leave_date = validated_data.get('leave_date')
        user_obj.user_type = validated_data.get('user_type')
        user_obj.license_no = validated_data.get('license_no')
        user_obj.license_region = validated_data.get('license_region')
        user_obj.company_id = validated_data.get('company_id')
        user_obj.save()
        return user_obj

    def update(self, instance, validated_data):
        instance_fields = ['username', 'email', 'password', 'group_id',
                           'first_name','address','mobile_no','city_name','state_name','postal_code',
                            'country_id','employee_no','job_title','start_date','leave_date','user_type','license_no',
                            'license_region','company_id'
                           ]
        for instance_field in instance_fields:
            if instance_field == "password":
                instance.set_password(validated_data.get('password'))
            elif validated_data.get(instance_field):
                instance.__setattr__(instance_field, validated_data.get(instance_field))

        instance.save()
        return instance

    def validate(self, data):
        id = data.get("id")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        first_name = data.get("first_name")

        check_obj=User.objects.filter(email=email)
        if check_obj:
            res = {"success": "false", "code": 601, "message": "email already in Use."}
            raise CustomValidation(res, 601)

        check_obj = User.objects.filter(username=username)
        if check_obj:
            res = {"success": "false", "code": 601, "message": "Username  already in Use."}
            raise CustomValidation(res, 601)


        if not email or not username or not first_name:
            res = {"success": "false", "code": 601, "message": "Error in post."}
            raise CustomValidation(res, 601)

        return data

    class Meta:
        fields = ['id', 'email', 'password', 'last_login', 'first_name', 'last_name', 'username', 'date_of_birth',
                  'group_id', 'mobile_no', 'address', 'city_name',
                  'state_name', 'postal_code', 'country_id', 'employee_no', 'job_title', 'start_date',
                  'leave_date', 'user_type', 'license_no', 'license_region', 'company_id']
        model = User
        read_only_fields = ('id',)
        write_only_fields = ('password',)
