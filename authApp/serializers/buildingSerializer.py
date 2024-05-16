from rest_framework import serializers
from authApp.models.building import Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = [
            'building_id',
            'name'
        ]

        read_only_fields = [
            'building_id'
        ]

        def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            locations = data.get('locations', [])
            for location in locations:
                if location.buildings.exclude(id=self.instance.id if self.instance else None).exists():
                    raise serializers.ValidationError(f"The location '{location}' is already assigned to another building.")
            return data