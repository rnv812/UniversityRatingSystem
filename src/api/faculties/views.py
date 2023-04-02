from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Faculty
from .serializers import FacultySerializer


class FacultyViewSet(ReadOnlyModelViewSet):
    queryset = Faculty.objects.all().order_by('pk')
    serializer_class = FacultySerializer
    permission_classes = (AllowAny, )
