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
            if data.get('long') <= 0 or data.get('high') <= 0 or data.get('width') <= 0:
                raise serializers.ValidationError("The long, high and width values must be positive.")
            if len(data.get('description', '')) > 250:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            return data