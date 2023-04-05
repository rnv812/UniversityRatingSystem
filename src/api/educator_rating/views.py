from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    SAFE_METHODS,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from api.educators.models import Educator
from api.educators.permissions import IsEducatorUser

from .mixins import PartialUpdateModelMixin
from .models import (
    EducatorIndicatorValue,
    EducatorRatingPartition,
    EducatorReport,
    EducatorReportController
)
from .permissions import (
    IsNotPrivilegedIndicatorOnPatch,
    IsOpenForUpdateValueOnPatch,
    IsOpenToDestroyReportOnDelete,
    IsOnlyValueUpdateOnPatch,
    IsReportControllerUser,
    IsReportOwnerUser,
    IsUnapprovedReportOnPost,
    IsValueControllerUser,
    IsValueOwnerUser,
)
from .serializers import (
    EducatorIndicatorValueSerializer,
    EducatorRatingPartitionSerializer,
    EducatorReportSerializer,
    EducatorReportControllerSerializer
)


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
        ((IsValueOwnerUser & IsNotPrivilegedIndicatorOnPatch)
         | IsValueControllerUser | IsAdminUser),
        IsOpenForUpdateValueOnPatch,
        IsOnlyValueUpdateOnPatch
    )


class EducatorReportViewSet(ModelViewSet):
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
        controlled by requesting user. If user is not a report
        controller request is not allowed.
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
