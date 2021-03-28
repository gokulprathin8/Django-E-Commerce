from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_image = models.ImageField()
    product_name = models.CharField(max_length=1024)
    product_price = models.PositiveIntegerField()
    product_availability_count = models.IntegerField()
    product_color = models.CharField(max_length=255)
    product_tax = models.PositiveIntegerField()
    product_description = models.TextField()
    product_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def compute_total_price(self):
        return self.product_price + self.product_tax