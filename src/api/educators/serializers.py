from rest_framework.serializers import ModelSerializer

from .models import Educator


class EducatorSerializer(ModelSerializer):
    class Meta:
        model = Educator
        fields = '__all__'
