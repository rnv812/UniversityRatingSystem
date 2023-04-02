from rest_framework.serializers import ModelSerializer

from .models import (EducatorRatingPartition,
                     EducatorIndicatorValue,
                     EducatorReport,
                     EducatorReportController)


class EducatorRatingPartitionSerializer(ModelSerializer):
    class Meta:
        model = EducatorRatingPartition
        fields = ('id', 'partition', )


class EducatorIndicatorValueSerializer(ModelSerializer):
    class Meta:
        model = EducatorIndicatorValue
        fields = ('id', 'indicator', 'report', 'value', )


class EducatorReportSerializer(ModelSerializer):
    class Meta:
        model = EducatorReport
        fields = ('id', 'uuid', 'educator', 'year', 'approved', )


class EducatorReportControllerSerializer(ModelSerializer):
    class Meta:
        model = EducatorReportController
        fields = ('id', 'user', 'department', )
