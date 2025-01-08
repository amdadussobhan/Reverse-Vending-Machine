from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from vending.views import CategoryView, ProductView, CartView, OrderView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("category", CategoryView, basename="category")
route.register("product", ProductView, basename="product")
route.register("cart", CartView, basename="cart")
route.register("order", OrderView, basename="order")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
