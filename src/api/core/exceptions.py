from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY


class UnprocessableEntity(APIException):
    status_code = HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = _('Cannot perform operation on specified entity.')
    default_code = 'unprocessable_entity'
