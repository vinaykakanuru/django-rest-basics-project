"""drfproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title = "DRF BASICS")



schema_view = get_schema_view(
   openapi.Info(
      title="DRF Basics",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', include('app.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    # path('api_documentation/', schema_view),

    # path('openapi', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),

    # path('api/documentation/', TemplateView.as_view(
    #     template_name='index.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='api_doc'),

    path('api_documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
