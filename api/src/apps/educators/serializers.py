from rest_framework.serializers import ModelSerializer

from .models import Educator, Qualification


class EducatorSerializer(ModelSerializer):
    class Meta:
        model = Educator
        fields = (
            'id', 'user', 'qualification', 'department',
        )


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'name', )
