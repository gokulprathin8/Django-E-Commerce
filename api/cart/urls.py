from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.UserCart, basename='getCart')
router.register('getCart', views.UserCartProducts, basename='userCartProducts')

urlpatterns = [
    path('', include(router.urls)),
    path('cartExists', views.userCartExists, name='userCartExists'),
    path('cartExists/change', views.userCartModifications, name='userCartModifications'),
]