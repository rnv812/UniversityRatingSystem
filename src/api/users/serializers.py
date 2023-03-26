from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = (
            'id', 'username', 'email', 'last_name', 'first_name', 'patronymic',
            'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login'
        )
