from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Educator, Qualification
from .serializers import EducatorSerializer, QualificationSerializer


class EducatorViewSet(ReadOnlyModelViewSet):
    queryset = Educator.objects.all().order_by('pk')
    serializer_class = EducatorSerializer
    permission_classes = (AllowAny, )


class QualificationViewSet(ReadOnlyModelViewSet):
    queryset = Qualification.objects.all().order_by('pk')
    serializer_class = QualificationSerializer
    permission_classes = (AllowAny, )
