from rest_framework.serializers import ModelSerializer
from .models import Category, Product, Cart, Order

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'