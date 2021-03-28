from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('getProducts/', views.ProductsView.as_view()),
]