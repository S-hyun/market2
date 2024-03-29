from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
class ProductLCView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommentListView(generics.ListAPIView):
    renderer_classes = {JSONRenderer}
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProductDetialView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer