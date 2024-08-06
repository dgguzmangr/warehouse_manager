from rest_framework import serializers
from authApp.models.location import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'location_id',
            'type',
            'long', 
            'high', 
            'width', 
            'weight', 
            'volume',
            'description'
        ]
        read_only_fields = [
            'location_id',
            'volume'
            ]
        
    def validate(self, data):
        if len(data.get('description', '')) > 250:
            raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
        if data.get('long', 1) <= 0:
            raise serializers.ValidationError({"long": "Long must be a positive number."})
        if data.get('high', 1) <= 0:
            raise serializers.ValidationError({"high": "High must be a positive number."})
        if data.get('width', 1) <= 0:
            raise serializers.ValidationError({"width": "Width must be a positive number."})
        if data.get('weight', 1) <= 0:
            raise serializers.ValidationError({"weight": "Weight must be a positive number."})
        return data