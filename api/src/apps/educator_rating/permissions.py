from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from apps.core.exceptions import UnprocessableEntity
from apps.core.shortcuts import get_object_or_error
from apps.educators.models import Educator
from apps.rating.validators import (IndicatorValueValidationError,
                                    validate_indicator_value)

from .models import (EducatorIndicatorValue, EducatorReport,
                     EducatorReportController)


class IsValueOwnerUser(BasePermission):
    message = _(
        "You cannot operate values of reports which are not owned by you "
        "or values of privileged indicators."
    )

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorIndicatorValue
    ) -> bool:
        return (obj.report.educator.user == request.user
                and not obj.indicator.privileged)


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
        if request.method == 'PATCH':
            match request.data:
                case {'value': dict(value)}:
                    try:
                        validate_indicator_value(value)
                    except IndicatorValueValidationError:
                        return False

                    return value['type'] == obj.value['type']
                case _:
                    return False

        return True


class IsReportOwnerUser(BasePermission):
    message = _(
        "You cannot operate reports which are not owned or controlled by you."
    )

    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == 'POST' and 'educator' in request.data:
            educator = get_object_or_error(
                exception=UnprocessableEntity(
                    detail=_('Specified educator is not found.')
                ),
                klass=Educator,
                pk=request.data['educator']
            )

            return request.user == educator.user

        return True

    def has_object_permission(
            self,
            request: Request,
            view: View,
            obj: EducatorReport
    ) -> bool:
        return obj.educator.user == request.user


class IsReportControllerUser(BasePermission):
    message = _(
        "You cannot operate reports which are not owned or controlled by you."
    )

    def has_permission(self, request: Request, view: View) -> bool:
        try:
            controller = EducatorReportController.objects.get(
                user=request.user
            )
        except EducatorReportController.DoesNotExist:
            return False

        if request.method == 'POST' and 'educator' in request.data:
            educator = get_object_or_error(
                exception=UnprocessableEntity(
                    detail=_('Specified educator is not found.'),
                ),
                klass=Educator,
                pk=request.data['educator']
            )

            return controller.department == educator.department

        return True

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


class IsUnapprovedReportOnPost(BasePermission):
    message = _(
        "You cannot create approved reports."
    )

    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == 'POST' and 'approved' in request.data:
            return request.data['approved'] is False

        return True


class IsOpenToDestroyReportOnDelete(BasePermission):
    message = _("You cannot delete already approved reports.")

    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: EducatorReport
    ) -> bool:
        if request.method == 'DELETE':
            return not obj.approved

        return True
