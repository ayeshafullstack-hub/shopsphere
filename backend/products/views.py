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
        
        #Category filtering
        category = self.request.query_params.get("category")
        
        if category:
            queryset = queryset.filter(category = category)
            
        #Price filtering
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_paramas.get("max_price")
        
        if min_price:
            queryset = queryset.filter(price_gte=min_price)
            
        if max_price:
            queryset = queryset.filter(price_lte=max_price)
        
        return queryset


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer