from rest_framework.viewsets import (ReadOnlyModelViewSet,
                                     ModelViewSet)
from rest_framework.permissions import (SAFE_METHODS,
                                        IsAdminUser,
                                        IsAuthenticated)
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from api.educators.permissions import IsEducator
from api.educators.models import Educator

from .models import (EducatorRatingPartition,
                     EducatorIndicatorValue,
                     EducatorReport,
                     EducatorReportController)
from .serializers import (EducatorRatingPartitionSerializer,
                          EducatorIndicatorValueSerializer,
                          EducatorReportSerializer,
                          EducatorReportControllerSerializer)
from .permissions import IsEducatorReportController


class EducatorRatingPartitionViewSet(ReadOnlyModelViewSet):
    queryset = EducatorRatingPartition.objects.all().order_by('pk')
    serializer_class = EducatorRatingPartitionSerializer


class EducatorIndicatorValueViewSet(ModelViewSet):
    queryset = EducatorIndicatorValue.objects.all().order_by('pk')
    serializer_class = EducatorIndicatorValueSerializer


class EducatorReportViewSet(ReadOnlyModelViewSet):
    queryset = EducatorReport.objects.all().order_by('pk')
    serializer_class = EducatorReportSerializer
    permission_classes = (IsAdminUser, )

    @action(
        detail=False,
        methods=SAFE_METHODS,
        permission_classes=(IsAuthenticated, IsEducator, )
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
        permission_classes=(IsAuthenticated, IsEducatorReportController, )
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


class EducatorReportControllerViewSet(ReadOnlyModelViewSet):
    queryset = EducatorReportController.objects.all().order_by('pk')
    serializer_class = EducatorReportControllerSerializer
    permission_classes = (IsAdminUser, )
