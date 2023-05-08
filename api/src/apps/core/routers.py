from rest_framework import routers

from apps.departments.views import DepartmentTypeViewSet, DepartmentViewSet
from apps.educator_rating.views import (EducatorIndicatorValueViewSet,
                                        EducatorRatingPartitionViewSet,
                                        EducatorReportControllerViewSet,
                                        EducatorReportViewSet)
from apps.educators.views import EducatorViewSet, QualificationViewSet
from apps.faculties.views import FacultyViewSet
from apps.rating.views import (CriterionViewSet, IndicatorViewSet,
                               RatingPartitionViewSet, ValueTypeViewSet)
from apps.users.views import AllowedEmailViewSet


api_router = routers.DefaultRouter()

# users app
api_router.register(
    prefix='allowed-emails',
    viewset=AllowedEmailViewSet,
    basename='allowed-email'
)

# faculties app
api_router.register(
    prefix='faculties',
    viewset=FacultyViewSet,
    basename='faculty'
)

# departments app
api_router.register(
    prefix='departments',
    viewset=DepartmentViewSet,
    basename='department'
)
api_router.register(
    prefix='department-types',
    viewset=DepartmentTypeViewSet,
    basename='department-type'
)

# educators app
api_router.register(
    prefix='educators',
    viewset=EducatorViewSet,
    basename='educator'
)
api_router.register(
    prefix='qualifications',
    viewset=QualificationViewSet,
    basename='qualification'
)

# rating app
api_router.register(
    prefix='value-types',
    viewset=ValueTypeViewSet,
    basename='value-type'
)
api_router.register(
    prefix='rating-partitions',
    viewset=RatingPartitionViewSet,
    basename='rating-partition'
)
api_router.register(
    prefix='indicators',
    viewset=IndicatorViewSet,
    basename='indicator'
)
api_router.register(
    prefix='criterions',
    viewset=CriterionViewSet,
    basename='criterion'
)

# educator_rating app
api_router.register(
    prefix='educator-partitions',
    viewset=EducatorRatingPartitionViewSet,
    basename='educator-partition'
)
api_router.register(
    prefix='educator-indicator-values',
    viewset=EducatorIndicatorValueViewSet,
    basename='educator-indicator-value'
)
api_router.register(
    prefix='educator-reports',
    viewset=EducatorReportViewSet,
    basename='educator-report'
)
api_router.register(
    prefix='educator-report-controllers',
    viewset=EducatorReportControllerViewSet,
    basename='educator-report-controller'
)
