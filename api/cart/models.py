from django.db import models
from django.contrib.auth.models import User

from ..products import models as productModels


class Cart(models.Model):
    current_user = models.OneToOneField(User, on_delete=models.CASCADE)
    # cart = models.ForeignKey(CartProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.current_user.username

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_products = models.OneToOneField(productModels.Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)