from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from .models import EducatorReportController


class IsEducatorReportController(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            EducatorReportController.objects.get(user=request.user)
            return True
        except EducatorReportController.DoesNotExist:
            return False
