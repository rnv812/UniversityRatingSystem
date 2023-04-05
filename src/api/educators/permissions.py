from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from .models import Educator


class IsEducator(BasePermission):
    message = _("You are not an educator.")

    def has_permission(self, request: Request, view: View) -> bool:
        try:
            Educator.objects.get(user=request.user)
            return True
        except Educator.DoesNotExist:
            return False
