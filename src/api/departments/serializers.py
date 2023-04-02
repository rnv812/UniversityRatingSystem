from rest_framework.serializers import ModelSerializer

from .models import Department, DepartmentType


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id', 'name', 'department_type',
            'head', 'faculty',
        )


class DepartmentTypeSerializer(ModelSerializer):
    class Meta:
        model = DepartmentType
        fields = ('id', 'name', )
