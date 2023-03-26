from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for Department model."""

    class Meta:
        model = models.Department
        fields = '__all__'
