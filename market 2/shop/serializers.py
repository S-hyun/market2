from .models import *

from rest_framework import serializers
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']

class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
"""
c94e3689c5c972bd8b37921231a2235a0362d445
"""