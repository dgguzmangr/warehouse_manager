from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from authApp.models.warehouse import Warehouse
from authApp.models.building import Building
from authApp.models.location import Location
from authApp.serializers.warehouseSerializer import WarehouseSerializer
from authApp.serializers.buildingSerializer import BuildingSerializer
from authApp.serializers.locationSerializer import LocationSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


# Warehouse API

@swagger_auto_schema(method='get', responses={200: WarehouseSerializer(many=True)} , tags=['Warehouse'])
@api_view(['GET'])
def show_warehouses(request):
    if request.method == 'GET':
        warehouse = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=WarehouseSerializer, responses={201: WarehouseSerializer}, tags=['Warehouse'])
@api_view(['POST'])
def create_warehouse(request):
    if request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=WarehouseSerializer, responses={200: WarehouseSerializer}, tags=['Warehouse'])
@api_view(['PUT'])
def update_warehouse(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=WarehouseSerializer, responses={200: WarehouseSerializer}, tags=['Warehouse'])
@api_view(['PATCH'])
def partial_update_warehouse(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = WarehouseSerializer(warehouse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Warehouse'])
@api_view(['DELETE'])
def delete_warehouse(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', responses={200: WarehouseSerializer(many=True)}, tags=['Warehouse'])
@api_view(['GET'])
def show_warehouse_buildings(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        building = Building.objects.get(warehouse=warehouse)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BuildingSerializer(building)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Building API

@swagger_auto_schema(method='get', responses={200: BuildingSerializer(many=True)} , tags=['Building'])
@api_view(['GET'])
def show_buildings(request):
    if request.method == 'GET':
        building = Building.objects.all()
        serializer = BuildingSerializer(building, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=BuildingSerializer, responses={201: BuildingSerializer}, tags=['Building'])
@api_view(['POST'])
def create_building(request):
    if request.method == 'POST':
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=BuildingSerializer, responses={200: BuildingSerializer}, tags=['Building'])
@api_view(['PUT'])
def update_building(request, pk):
    try:
        building = Building.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=BuildingSerializer, responses={200: BuildingSerializer}, tags=['Building'])
@api_view(['PATCH'])
def partial_update_building(request, pk):
    try:
        building = Building.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = BuildingSerializer(building, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Building'])
@api_view(['DELETE'])
def delete_building(request, pk):
    try:
        building = BuildingSerializer.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', responses={200: BuildingSerializer(many=True)}, tags=['Building'])
@api_view(['GET'])
def show_building_locations(request, pk):
    try:
        building = Building.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        location = Location.objects.get(building=building)
    except Location.DoesNotExist:
        return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LocationSerializer(building)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Location API

@swagger_auto_schema(method='get', responses={200: LocationSerializer(many=True)} , tags=['Location'])
@api_view(['GET'])
def show_locations(request):
    if request.method == 'GET':
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=LocationSerializer, responses={201: LocationSerializer}, tags=['Location'])
@api_view(['POST'])
def create_location(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=LocationSerializer, responses={200: LocationSerializer}, tags=['Location'])
@api_view(['PUT'])
def update_location(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='patch', request_body=LocationSerializer, responses={200: LocationSerializer}, tags=['Location'])
@api_view(['PATCH'])
def partial_update_location(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = LocationSerializer(location, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Location'])
@api_view(['DELETE'])
def delete_location(request, pk):
    try:
        location = LocationSerializer.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Login API

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user')
        }
    ),
    responses={
        200: openapi.Response(
            description="Successful login",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token')
                }
            )
        ),
        400: openapi.Response(
            description="Invalid username or password",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
                }
            )
        )
    },
    tags=['Authentication']
)
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)