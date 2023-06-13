from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import AllowedEmail
from .serializers import AllowedEmailSerializer


class AllowedEmailViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = AllowedEmail.objects.all().order_by('pk')
    serializer_class = AllowedEmailSerializer
    permission_classes = (IsAdminUser, )
