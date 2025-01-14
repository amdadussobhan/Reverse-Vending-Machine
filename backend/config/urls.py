from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
