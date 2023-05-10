from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Educator, Qualification
from .permissions import IsEducatorUser
from .serializers import EducatorSerializer, QualificationSerializer


class EducatorViewSet(ReadOnlyModelViewSet):
    queryset = Educator.objects.all().order_by('pk')
    serializer_class = EducatorSerializer

    @action(
        detail=False,
        methods=SAFE_METHODS,
        permission_classes=(IsAuthenticated, IsEducatorUser, )
    )
    def me(self, request: Request) -> Response:
        """Get educator instance of requested user."""

        return Response(
            EducatorSerializer(
                instance=Educator.objects.get(user=request.user)
            ).data
        )


class QualificationViewSet(ReadOnlyModelViewSet):
    queryset = Qualification.objects.all().order_by('pk')
    serializer_class = QualificationSerializer
