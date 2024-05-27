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
from authApp.views import businessModelView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Warehouse Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # warehouse urls
    path('show-warehouses/', appView.show_warehouses, name='List all created warehouses'),
    path('create-warehouse/', appView.create_warehouse, name='Create a new warehouse'),
    path('update-warehouse/<int:pk>/', appView.update_warehouse, name='Update a selected warehouse'),
    path('patial-update-warehouse/<int:pk>/', appView.partial_update_warehouse, name='Update a selected attribute for a warehouse'),
    path('delete-warehouse/<int:pk>/', appView.delete_warehouse, name='Delete a selected warehouse'),
    path('show-warehouse-buildings/<int:pk>/', appView.show_warehouse_buildings, name='List all buildings by warehouse'),

    # building urls
    path('show-buildings/', appView.show_buildings, name='List all created buildings'),
    path('create-building/', appView.create_building, name='Create a new building'),
    path('update-building/<int:pk>/', appView.update_building, name='Update a selected building'),
    path('patial-update-building/<int:pk>/', appView.partial_update_building, name='Update a selected attribute for a building'),
    path('delete-building/<int:pk>/', appView.delete_building, name='Delete a selected building'),
    path('show-building-locations/<int:pk>/', appView.show_building_locations, name='List all locations by building'),

    # location urls
    path('show-locations/', appView.show_locations, name='List all created locations'),
    path('create-location/', appView.create_location, name='Create a new location'),
    path('update-location/<int:pk>/', appView.update_location, name='Update a selected location'),
    path('patial-update-location/<int:pk>/', appView.partial_update_location, name='Update a selected attribute for a location'),
    path('delete-location/<int:pk>/', appView.delete_location, name='Delete a selected location'),

    # Business Model url
    path('field-structure-view/', businessModelView.field_structure_view, name='Generate a json structure for all models'),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/
