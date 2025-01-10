from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from vending.views import CategoryView, ProductView, CartView, OrderView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("categories", CategoryView, basename="categories")
route.register("products", ProductView, basename="products")
route.register("carts", CartView, basename="carts")
route.register("orders", OrderView, basename="orders")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/', include(route.urls)),
]
