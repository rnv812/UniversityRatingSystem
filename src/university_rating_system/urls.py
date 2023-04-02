"""university_rating_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.schemas import get_schema_view

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
api_router.register(
    prefix='users',
    viewset=UserViewSet,
    basename='user'
)
api_router.register(
    prefix='faculties',
    viewset=FacultyViewSet,
    basename='faculty'
)
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include(api_router.urls)),
]

urlpatterns_debug = [
    path(
        'api/v1/schema/',
        get_schema_view(
            title='API Schema',
            version=1,
        ),
        name='api_schema'
    ),
    path(
        'api/v1/swagger/',
        TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'api_schema'}
        ),
        name='swagger'
    ),
]

if settings.DEBUG:
    urlpatterns.extend(urlpatterns_debug)
