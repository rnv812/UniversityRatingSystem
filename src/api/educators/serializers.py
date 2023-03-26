from rest_framework import serializers

from . import models


class EducatorSerializer(serializers.ModelSerializer):
    """Serializer for Educator model."""

    class Meta:
        model = models.Educator
        fields = '__all__'
