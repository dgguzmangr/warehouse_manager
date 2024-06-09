from rest_framework import serializers
from authApp.models.warehouse import Warehouse
from authApp.models.building import Building

class WarehouseSerializer(serializers.ModelSerializer):
    building = serializers.PrimaryKeyRelatedField(queryset=Building.objects.all(), required=True)
    class Meta:
        model = Warehouse
        fields = [
            'warehouse_id',
            'name',
            'country',
            'department',
            'city',
            'neighborthood',
            'address',
            'postal_code',
            'location',
            'building',
        ]

        read_only_fields = [
            'warehouse_id',
            'building'
        ]

        def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            if len(data.get('country', '')) > 30:
                raise serializers.ValidationError("The 'country' field cannot exceed 100 characters.")
            if len(data.get('department', '')) > 100:
                raise serializers.ValidationError("The 'department' field cannot exceed 100 characters.")
            if len(data.get('neighborthood', '')) > 100:
                raise serializers.ValidationError("The 'neighborthood' field cannot exceed 100 characters.")
            if len(data.get('address', '')) > 200:
                raise serializers.ValidationError("The 'address' field cannot exceed 200 characters.")
            if len(data.get('posta_code', '')) > 20:
                raise serializers.ValidationError("The 'postal code' field cannot exceed 20 characters.")
            buildings = data.get('buildings', [])
            for building in buildings:
                if building.warehouses.exclude(id=self.instance.id if self.instance else None).exists():
                    raise serializers.ValidationError(f"The building '{building}' is already assigned to another warehouse.")
            return data