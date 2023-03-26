from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Faculty
from .serializers import FacultySerializer


class FacultyViewSet(ReadOnlyModelViewSet):
    """Faculty view set that only allows to read all faculty instances
    for all users (including unauthorized).
    """

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (AllowAny, )
