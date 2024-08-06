from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Location
from .serializers import LocationSerializer

class LocationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.location1 = Location.objects.create(
            type='Pasillo', long=10.0, high=5.0, width=2.0, weight=500.0, description='Pasillo 1'
        )
        self.location2 = Location.objects.create(
            type='Estantería', long=8.0, high=4.0, width=1.5, weight=300.0, description='Estantería 1'
        )

    def test_show_locations(self):
        response = self.client.get(reverse('List all created locations'))
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_show_locations_empty(self):
        Location.objects.all().delete()
        response = self.client.get(reverse('List all created locations'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_create_location_valid(self):
        data = {
            'type': 'Pasillo',
            'long': 10.0,
            'high': 5.0,
            'width': 2.0,
            'weight': 500.0,
            'description': 'Pasillo de prueba'
        }
        response = self.client.post(reverse('Create a new location'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        location = Location.objects.get(location_id=response.data['location_id'])
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)

    def test_create_location_invalid(self):
        data = {
            'long': 10.0,
            'high': 5.0,
            'width': 2.0,
            'weight': 500.0,
            'description': 'Pasillo de prueba'
        }
        response = self.client.post(reverse('Create a new location'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('type', response.data)

    def test_update_location_valid(self):
        data = {
            'type': 'Rack',
            'long': 12.0,
            'high': 6.0,
            'width': 2.5,
            'weight': 600.0,
            'description': 'Rack actualizado'
        }
        response = self.client.put(reverse('Update a selected location', args=[self.location1.location_id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        location = Location.objects.get(location_id=self.location1.location_id)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)

    def test_update_location_not_found(self):
        data = {
            'type': 'Rack',
            'long': 12.0,
            'high': 6.0,
            'width': 2.5,
            'weight': 600.0,
            'description': 'Rack actualizado'
        }
        response = self.client.put(reverse('Update a selected location', args=[999]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Location not found"})

    def test_partial_update_location_valid(self):
        data = {
            'description': 'Pasillo parcialmente actualizado'
        }
        response = self.client.patch(reverse('Update a selected attribute for a location', args=[self.location1.location_id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        location = Location.objects.get(location_id=self.location1.location_id)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(location.description, 'Pasillo parcialmente actualizado')

    def test_partial_update_location_invalid(self):
        data = {
            'long': -10.0
        }
        response = self.client.patch(reverse('Update a selected attribute for a location', args=[self.location1.location_id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('long', response.data)

    def test_partial_update_location_not_found(self):
        data = {
            'description': 'Descripción no encontrada'
        }
        response = self.client.patch(reverse('Update a selected attribute for a location', args=[999]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Location not found"})

    def test_delete_location_valid(self):
        response = self.client.delete(reverse('Delete a selected location', args=[self.location1.location_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Location.DoesNotExist):
            Location.objects.get(location_id=self.location1.location_id)

    def test_delete_location_not_found(self):
        response = self.client.delete(reverse('Delete a selected location', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Location not found"})