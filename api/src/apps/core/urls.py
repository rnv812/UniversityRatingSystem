from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    from django.urls import re_path

    from rest_framework.permissions import AllowAny

    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

from .routers import api_router

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include((api_router.urls, 'api'), namespace='api')),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="University Rating System API",
            default_version='v1',
            description="API for performing operations on rating reports.",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="nikita.reznikov.public@mail.ru"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=(AllowAny, ),
    )

    urlpatterns_debug = [
        re_path(
            r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'
        ),
        re_path(
            r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
        ),
        re_path(
            r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
        ),
    ]

    urlpatterns.extend(urlpatterns_debug)
