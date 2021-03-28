from django.contrib import admin

from . import models

class CartProductsInline(admin.TabularInline):
    model = models.CartProducts

class TabularInlineAdmin(admin.ModelAdmin):
    inlines = [CartProductsInline, ]
    list_display = ['current_user', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(models.Cart, TabularInlineAdmin)