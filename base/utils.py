from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.encoding import force_text


class CustomValidation(APIException):
    default_detail = 'A server error occurred.'
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, return_dict, status_code):
        if status_code is not None: self.status_code = status_code
        if return_dict is not None:
            self.detail = return_dict
        else:
            self.detail = {'detail': force_text(self.default_detail)}