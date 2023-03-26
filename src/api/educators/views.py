from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Educator, Qualification
from .serializers import EducatorSerializer, QualificationSerializer


class EducatorViewSet(ReadOnlyModelViewSet):
    """Educator view set that only allows to read all educator instances
    for all users (including unauthorized).
    """

    queryset = Educator.objects.all().order_by('pk')
    serializer_class = EducatorSerializer
    permission_classes = (AllowAny, )

    @action(detail=False, methods=SAFE_METHODS, permission_classes=(AllowAny, ))
    def qualifications(self, request: Request) -> Response:
        return Response(
            QualificationSerializer(
                instance=Qualification.objects.all().order_by('pk'),
                many=True
            ).data
        )
