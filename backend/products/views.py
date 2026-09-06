from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    ## queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ["name","description"]
    
    def get_queryset(self):
        queryset = Product.objects.all()
        
        category = self.request.query_params.get("category")
        
        if category:
            queryset = queryset.filter(category = category)
        
        return queryset


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer