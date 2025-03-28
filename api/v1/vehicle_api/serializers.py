from rest_framework import serializers
from vehicles.models import Category, Vehicle, Variant, VehiclePrice

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'category', 'year', 'make']

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'name', 'vehicle']

class VehiclePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePrice
        fields = ['id', 'variant', 'price', 'currency']
