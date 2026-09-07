from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    ## queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name","description"]
    
    ordering_fields = [
        "price",
        "created_at",
        "name",
    ]
    
    def get_queryset(self):
        queryset = Product.objects.all()
        
        #Category filtering
        category = self.request.query_params.get("category")
        
        if category:
            queryset = queryset.filter(category = category)
            
        #Stock filtering
        in_stock = self.request.query_params.get("in_stock")
        
        if in_stock == "true":
            queryset = queryset.filter(stock__gt=0)
            
        #Price filtering
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
            
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        
        if self.request.method == "DELETE":
            return [IsAdminUser()]
        return [IsAuthenticated()]