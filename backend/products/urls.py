from django.urls import path
from .views import ProductListCreateAPIView
from .views import ProductDetailAPIView

urlpatterns = [
    path("products/",ProductListCreateAPIView.as_view(),name="product-list"),
    path("products/<int:pk>/",ProductDetailAPIView.as_view(),name="product-detail"),
]
