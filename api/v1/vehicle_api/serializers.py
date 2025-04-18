from rest_framework import serializers
from vehicles.models import Category, Vehicle, Variant, VehiclePrice

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class VehicleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Show category details in response
    category_id = serializers.IntegerField(write_only=True)  # Accept category ID for updates

    class Meta:
        model = Vehicle
        fields = ['id', 'title', 'category', 'category_id', 'description', 'uploaded_at']
        read_only_fields = ['uploaded_at']

    def create(self, validated_data):
        """Create a new Vehicle instance."""
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)  
        vehicle = Vehicle.objects.create(category=category, **validated_data)  
        return vehicle

    def update(self, instance, validated_data):
        """Update an existing Vehicle instance."""
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            instance.category = Category.objects.get(id=category_id)
           # Update other fields dynamically
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class VariantSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField(read_only=True)  # Read-only vehicle details
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle', write_only=True)

    class Meta:
        model = Variant
        fields = ['id', 'vehicle', 'vehicle_id', 'title', 'description', 'color', 'image_category', 'image_file']


class VehiclePriceSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField(read_only=True)  # Show vehicle name in response
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle', write_only=True)

    class Meta:
        model = VehiclePrice
        fields = ['id', 'vehicle', 'vehicle_id', 'spec_type', 'color', 'price']
