from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import CategorySerializer, VehicleSerializer, VariantSerializer, VehiclePriceSerializer
from vehicles.models import Category, Vehicle, Variant, VehiclePrice
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([AllowAny])
def get_category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:    
        return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT) 

# -----------------------------------------------------------------------------------------------------------------


@api_view(['GET'])
@permission_classes([AllowAny])
def get_vehicle_list(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_vehicle_by_id(request, id):
    try:
        vehicle = Vehicle.objects.get(pk=id)
    except Vehicle.DoesNotExist:
        return Response({"message": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def create_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_vehicle(request, vehicle_id):
    """Update a vehicle fully."""
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

    vehicle.delete()    
    return Response({"message": "Vehicle deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_variant_list(request):
    variants = Variant.objects.all()
    serializer = VariantSerializer(variants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_variant(request):
    serializer = VariantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_variant(request, variant_id):
    try:
        variant = Variant.objects.get(id=variant_id)
    except Variant.DoesNotExist:
        return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = VariantSerializer(variant, data=request.data, partial=True)  # Allow partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete variants
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_variant(request, variant_id):
    try:
        variant = Variant.objects.get(id=variant_id)
    except Variant.DoesNotExist:
        return Response({"error": "Variant not found"}, status=status.HTTP_404_NOT_FOUND)

    variant.delete()    
    return Response({"message": "Variant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_vehicle_price_list(request):
    prices = VehiclePrice.objects.all()
    serializer = VehiclePriceSerializer(prices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vehicle_price(request):
    serializer = VehiclePriceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_vehicle_prices(request):
    prices = VehiclePrice.objects.all()
    serializer = VehiclePriceSerializer(prices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_vehicle_price(request, price_id):
    try:
        price = VehiclePrice.objects.get(id=price_id)
    except VehiclePrice.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = VehiclePriceSerializer(price, data=request.data, partial=True) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_vehicle_price(request, price_id):
    try:
        price = VehiclePrice.objects.get(id=price_id)
    except VehiclePrice.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)

    price.delete()
    return Response({"message": "Vehicle price deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



