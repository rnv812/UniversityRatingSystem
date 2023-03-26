from rest_framework.serializers import ModelSerializer

from .models import Educator


class EducatorSerializer(ModelSerializer):
    class Meta:
        model = Educator
        fields = ('id', 'user_id', 'qualification_id', 'department_id', )
