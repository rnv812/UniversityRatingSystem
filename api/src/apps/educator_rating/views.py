from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import (SAFE_METHODS, IsAdminUser,
                                        IsAuthenticated)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from apps.educators.models import Educator
from apps.educators.permissions import IsEducatorUser

from .brokers import send_educator_report_to_broker
from .mixins import PartialUpdateModelMixin
from .models import (EducatorIndicatorValue, EducatorRatingPartition,
                     EducatorReport, EducatorReportController)
from .permissions import (IsOnlyValueUpdateOnPatch,
                          IsOpenForUpdateValueOnPatch,
                          IsOpenToDestroyReportOnDelete,
                          IsReportControllerUser, IsReportOwnerUser,
                          IsUnapprovedReportOnPost, IsValueControllerUser,
                          IsValueOwnerUser)
from .serializers import (EducatorIndicatorValueSerializer,
                          EducatorRatingPartitionSerializer,
                          EducatorReportControllerSerializer,
                          EducatorReportSerializer)


class EducatorRatingPartitionViewSet(ReadOnlyModelViewSet):
    queryset = EducatorRatingPartition.objects.all().order_by('pk')
    serializer_class = EducatorRatingPartitionSerializer


class EducatorReportControllerViewSet(ReadOnlyModelViewSet):
    queryset = EducatorReportController.objects.all().order_by('pk')
    serializer_class = EducatorReportControllerSerializer


class EducatorIndicatorValueViewSet(RetrieveModelMixin,
                                    PartialUpdateModelMixin,
                                    GenericViewSet):
    queryset = EducatorIndicatorValue.objects.all().order_by('pk')
    serializer_class = EducatorIndicatorValueSerializer
    permission_classes = (
        IsAuthenticated,
        IsValueOwnerUser | IsValueControllerUser | IsAdminUser,
        IsOpenForUpdateValueOnPatch,
        IsOnlyValueUpdateOnPatch
    )

    @action(
        detail=True,
        methods=SAFE_METHODS,
        permission_classes=(
            IsAuthenticated,
            IsReportOwnerUser | IsReportControllerUser | IsAdminUser,
        )
    )
    def report_values(self, request: Request, pk: str) -> Response:
        """Get list of values of specified report."""
        report = get_object_or_404(EducatorReport, pk=pk)
        indicator_values = EducatorIndicatorValue.objects.filter(
            report=report
        ).order_by('pk')

        return Response(
            EducatorIndicatorValueSerializer(
                instance=indicator_values,
                many=True
            ).data
        )


class EducatorReportViewSet(RetrieveModelMixin,
                            CreateModelMixin,
                            DestroyModelMixin,
                            GenericViewSet):
    queryset = EducatorReport.objects.all().order_by('pk')
    serializer_class = EducatorReportSerializer
    permission_classes = (
        IsAuthenticated,
        IsReportOwnerUser | IsReportControllerUser | IsAdminUser,
        IsUnapprovedReportOnPost,
        IsOpenToDestroyReportOnDelete,
    )

    @action(
        detail=False,
        methods=SAFE_METHODS,
        permission_classes=(IsAuthenticated, IsEducatorUser, )
    )
    def my(self, request: Request) -> Response:
        """Get list of educator own reports. If user is not an educator
        request is not allowed.
        """

        return Response(
            EducatorReportSerializer(
                instance=EducatorReport.objects.filter(
                    educator=Educator.objects.get(user=request.user)
                ),
                many=True
            ).data
        )

    @action(
        detail=False,
        methods=SAFE_METHODS,
        permission_classes=(IsAuthenticated, IsReportControllerUser, )
    )
    def controlled(self, request: Request) -> Response:
        """Get list of educator reports at the department which is
        controlled by requesting user. Note that response also
        includes user own reports if he is an educator on this department.
        If user is not a report controller request is not allowed.
        """

        department_ids = EducatorReportController.objects.filter(
            user=request.user
        ).values_list('department_id', flat=True)
        educators = Educator.objects.filter(department_id__in=department_ids)

        return Response(
            EducatorReportSerializer(
                instance=EducatorReport.objects.filter(
                    educator__in=educators
                ),
                many=True
            ).data
        )

    @action(
        detail=True,
        methods=('PATCH',),
        permission_classes=(
            IsAuthenticated,
            IsReportControllerUser | IsAdminUser,
        )
    )
    def set_status(self, request: Request, pk: str) -> Response:
        """Change report approval status. Expected only `approved` field in
        request body with `true` or `false` values.
        """

        current_status = EducatorReport.objects.get(pk=pk).approved
        new_status = request.data.get('approved', current_status)

        # using filter with update cause of save violates unique constraint
        report = EducatorReport.objects.filter(pk=pk)

        if new_status != current_status:
            report.update(approved=new_status)

        report = report.first()

        # if report becomes approved we send it to broker
        if new_status is True:
            send_educator_report_to_broker(report)

        return Response(EducatorReportSerializer(instance=report).data)
