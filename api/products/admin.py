from django.contrib import admin
from . import models
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    def productImage(self, object):
        return format_html('<img src="{}" width="100" />'.format(object.product_image.url))

    def totalPrice(self, object):
        return object.compute_total_price()

    model = models.Product
    list_display = ('productImage', 'product_name', 'product_price', 'totalPrice', 'product_availability_count', 'product_created_by', 'created_at', 'updated_at')

admin.site.register(models.Product, ProductAdmin)