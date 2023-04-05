from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from .models import (
    EducatorIndicatorValue,
    EducatorReportController,
)


class IsEducatorReportController(BasePermission):
    message = _("You are not a controller of educator reports.")

    def has_permission(self, request: Request, view: View) -> bool:
        try:
            EducatorReportController.objects.get(user=request.user)
            return True
        except EducatorReportController.DoesNotExist:
            return False


class IsValueOwner(BasePermission):
    message = _(
        "You can operate only values of reports owned by you."
    )

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorIndicatorValue
    ) -> bool:
        return obj.report.educator.user == request.user


class IsValueController(BasePermission):
    message = _(
        "You can operate only values of reports controlled by you."
    )

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorIndicatorValue
    ) -> bool:
        try:
            controller = EducatorReportController.objects.get(
                user=request.user
            )
        except EducatorReportController.DoesNotExist:
            return False

        return controller.department == obj.report.educator.department


class IsOpenForEditValueOnPatch(BasePermission):
    message = _("You cannot edit values of report which is already approved.")

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorIndicatorValue
    ) -> bool:
        if request.method != 'PATCH':
            return True

        return not obj.report.approved


class IsOnlyValueChangedOnPatch(BasePermission):
    message = _("You can edit value only.")

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorIndicatorValue
    ) -> bool:
        if request.method != 'PATCH':
            return True

        changes = request.data.keys()
        if changes == ['value'] and isinstance(request.data['value'], dict):
            return obj.value['type'] == request.data['value'].get('type', None)
        else:
            return False


class HasEducatorReportAccess(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        print(request.data)
        return False
