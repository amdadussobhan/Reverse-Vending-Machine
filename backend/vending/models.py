from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    session_id = models.CharField(max_length=255)  # Used to track cart per session
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)  # Optional

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending')
    cart_items = models.ManyToManyField(Cart)

    def __str__(self):
        return f"Order {self.id} by {self.user}"
