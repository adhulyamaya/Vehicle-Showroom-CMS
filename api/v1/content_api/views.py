from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.utils.translation import gettext_lazy as _
from main.management.commands.create_roles_and_permissions import IsMainAdmin,IsSecondaryAdmin
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer,ShowroomSerializer
from content.models import Blog,Showroom


import logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_blog_list(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.filter(is_active=True, is_deleted=False)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes(IsAuthenticated)
def update_blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response({"message": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes(IsAuthenticated)
def delete_blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response({"message": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

    blog.delete()
    return Response({"message": "Blog deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_showroom_list(request):
    showrooms = Showroom.objects.all()
    serializer = ShowroomSerializer(showrooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# create showroom
@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_showroom(request):
    serializer = ShowroomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes(IsAuthenticated)
def update_showroom(request, id):
    try:
        showroom = Showroom.objects.get(pk=id)
    except Showroom.DoesNotExist:
        return Response({"message": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ShowroomSerializer(showroom, data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes(IsAuthenticated)
def delete_showroom(request, id):
    try:
        showroom = Showroom.objects.get(pk=id)
    except Showroom.DoesNotExist:
        return Response({"message": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND)

    showroom.delete()
    return Response({"message": "Showroom deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

