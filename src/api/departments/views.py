from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    """Department view set that only allows to read all department instances
    for all users (including unauthorized).
    """

    queryset = Department.objects.all().order_by('pk')
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )
