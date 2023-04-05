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
        if request.method == 'PATCH':
            return not obj.report.approved
        else:
            return True


class IsOnlyValuePartChangedOnPatch(BasePermission):
    message = _("You can only edit value field.")

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorIndicatorValue
    ) -> bool:
        if request.method == 'PATCH':
            return set(request.data.keys()) == set(['value'])
        else:
            return True


class HasEducatorReportAccess(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        print(request.data)
        return False