from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Cart, Order
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, OrderSerializer

# this is model view approach
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer