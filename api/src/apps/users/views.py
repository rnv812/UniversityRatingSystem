from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import AllowedEmail
from .serializers import AllowedEmailSerializer


class AllowedEmailViewSet(ModelViewSet):
    queryset = AllowedEmail.objects.all().order_by('pk')
    serializer_class = AllowedEmailSerializer
    permission_classes = (IsAdminUser, )
