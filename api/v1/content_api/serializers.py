from rest_framework import serializers
from content.models import Blog, Showroom
from rest_framework.serializers import ModelSerializer


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['creator', 'updator', 'is_deleted','is_blocked']
   
class ShowroomSerializer(ModelSerializer):
    class Meta:
        model = Showroom
        exclude = ['creator', 'updator', 'is_deleted','is_blocked']