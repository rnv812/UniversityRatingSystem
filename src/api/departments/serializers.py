from rest_framework.serializers import ModelSerializer

from .models import Department, DepartmentType


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'department_type_id', 'head_id', 'faculty_id', )


class DepartmentTypeSerializer(ModelSerializer):
    class Meta:
        model = DepartmentType
        fields = ('id', 'name', )
