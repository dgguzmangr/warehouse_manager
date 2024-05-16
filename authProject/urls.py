"""
URL configuration for authProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # comentar par deshabilitar seguridad
from rest_framework.authtoken import views
from authApp.views import appView
# from authApp.views import businessModelView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Warehouse Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # warehouse urls
    path('show-warehouses/', appView.show_warehouses),
    path('create-warehouse/', appView.create_warehouse),
    path('update-warehouse/<int:pk>/', appView.update_warehouse),
    path('delete-warehouse/<int:pk>/', appView.delete_warehouse),
    path('show-warehouse-buildings/<int:pk>/', appView.show_warehouse_buildings),

    # building urls
    path('show-buildings/', appView.show_buildings),
    path('create-building/', appView.create_building),
    path('update-building/<int:pk>/', appView.update_building),
    path('delete-building/<int:pk>/', appView.delete_building),
    path('show-building-locations/<int:pk>/', appView.show_building_locations),

    # location urls
    path('show-locations/', appView.show_locations),
    path('create-location/', appView.create_location),
    path('update-location/<int:pk>/', appView.update_location),
    path('delete-location/<int:pk>/', appView.delete_location),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/
