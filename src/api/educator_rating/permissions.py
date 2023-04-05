from django.utils.translation import gettext_lazy as _

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from .models import (
    EducatorIndicatorValue,
    EducatorReport,
    EducatorReportController,
)


class IsValueOwnerUser(BasePermission):
    message = _(
        "You cannot operate values of reports which are not owned by you."
    )

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorIndicatorValue
    ) -> bool:
        return obj.report.educator.user == request.user


class IsValueControllerUser(BasePermission):
    message = _(
        "You cannot operate values of reports which are not controlled by you."
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


class IsOpenForUpdateValueOnPatch(BasePermission):
    message = _("You cannot edit values of already approved report.")

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorIndicatorValue
    ) -> bool:
        if request.method != 'PATCH':
            return True

        return not obj.report.approved


class IsOnlyValueUpdateOnPatch(BasePermission):
    message = _("You cannot edit anything except value.")

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


class IsNotPrivilegedIndicatorOnPatch(BasePermission):
    message = _("You cannot edit values of privileged indicators.")

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorIndicatorValue
    ) -> bool:
        return not obj.indicator.privileged


class IsReportOwnerUser(BasePermission):
    message = _(
        "You cannot operate reports which are not owned by you."
    )

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorReport
    ) -> bool:
        return obj.educator.user == request.user


class IsReportControllerUser(BasePermission):
    message = _(
        "You cannot operate reports which are not controlled by you."
    )

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorReport
    ) -> bool:
        try:
            controller = EducatorReportController.objects.get(
                user=request.user
            )
        except EducatorReportController.DoesNotExist:
            return False

        return controller.department == obj.educator.department


class IsOpenToDestroyReportOnDelete(BasePermission):
    message = _(
        "You cannot delete already approved reports."
    )

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorReport
    ) -> bool:
        if request.method != 'DELETE':
            return True

        return not obj.approved


class IsUnapprovedReportOnPost(BasePermission):
    message = _(
        "You cannot create approved reports."
    )

    def has_permission(self, request: Request, view: View) -> bool:
        if request.method != 'POST':
            return True

        if 'approved' not in request.data:
            return True

        return request.data['approved'] is False
