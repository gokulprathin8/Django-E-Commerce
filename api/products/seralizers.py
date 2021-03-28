from rest_framework import serializers
from . import models

class ProductSeralizer(serializers.ModelSerializer):
    # product_name = models.CharField(max_length=1024)
    # product_price = models.PositiveIntegerField()
    # product_availability_count = models.IntegerField()
    # product_color = models.CharField(max_length=255)
    # product_tax = models.PositiveIntegerField()
    # product_description = models.TextField()

    class Meta:
        model = models.Product
        # fields = ('product_name', 'product_price', 'product_availability_count', 'product_color', 'product_tax', 'product_description')
        fields = "__all__"