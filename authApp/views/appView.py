from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.models.warehouse import Warehouse
from authApp.models.building import Building
from authApp.serializers.warehouseSerializer import WarehouseSerializer
from authApp.serializers.buildingSerializer import BuildingSerializer

from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad


# Warehouse API

@api_view(['GET'])
def show_warehouses(request):
    if request.method == 'GET':
        warehouse = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_warehouse(request):
    if request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['DELETE'])
def delete_warehouse(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def show_warehouse_buildings(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
    buildings = Building.objects.filter(warehouse=warehouse)
    serializer = BuildingSerializer(buildings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Building API

@api_view(['GET'])
def show_buildings(request):
    if request.method == 'GET':
        building = Building.objects.all()
        serializer = BuildingSerializer(building, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_building(request):
    if request.method == 'POST':
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['DELETE'])
def delete_building(request, pk):
    try:
        building = BuildingSerializer.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        building.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Login API

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)