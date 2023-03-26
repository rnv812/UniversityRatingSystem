from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Educator
from .serializers import EducatorSerializer


class EducatorViewSet(ReadOnlyModelViewSet):
    """Educator view set that only allows to read all educator instances
    for all users (including unauthorized).
    """

    queryset = Educator.objects.all().order_by('pk')
    serializer_class = EducatorSerializer
    permission_classes = (AllowAny, )
