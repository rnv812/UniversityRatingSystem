from rest_framework import routers

from api.users.views import UserViewSet
from api.faculties.views import FacultyViewSet
from api.departments.views import DepartmentViewSet, DepartmentTypeViewSet
from api.educators.views import EducatorViewSet, QualificationViewSet
from api.rating.views import (ValueTypeViewSet,
                              RatingPartitionViewSet,
                              IndicatorViewSet,
                              CriterionViewSet)
from api.educator_rating.views import (EducatorRatingPartitionViewSet,
                                       EducatorIndicatorValueViewSet,
                                       EducatorReportViewSet,
                                       EducatorReportControllerViewSet)


api_router = routers.DefaultRouter()

# users app
api_router.register(
    prefix='users',
    viewset=UserViewSet,
    basename='user'
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
