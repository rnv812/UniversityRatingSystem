from rest_framework import serializers

from . import models


class FacultySerializer(serializers.ModelSerializer):
    """Serializer for Faculty model."""

    class Meta:
        model = models.Faculty
        fields = ('name', 'head')
