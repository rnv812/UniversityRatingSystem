from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Educator, Qualification
from .serializers import EducatorSerializer, QualificationSerializer


class EducatorViewSet(ReadOnlyModelViewSet):
    queryset = Educator.objects.all().order_by('pk')
    serializer_class = EducatorSerializer


class QualificationViewSet(ReadOnlyModelViewSet):
    queryset = Qualification.objects.all().order_by('pk')
    serializer_class = QualificationSerializer
