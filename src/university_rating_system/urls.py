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

from rest_framework.schemas import get_schema_view

from .routers import api_router

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
