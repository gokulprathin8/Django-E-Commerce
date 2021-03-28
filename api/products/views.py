from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from . import models
from . import seralizers

class ProductsView(APIView):
    seralizer_class = seralizers.ProductSeralizer

    def get(self, request, format=None):
        data = models.Product.objects.all()
        data_s = seralizers.ProductSeralizer(data)
        return Response(data_s.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = seralizers.ProductSeralizer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def retrieve(self, request, *args, **kwargs):
        data = models.Product.objects.all()
        data_s = seralizers.ProductSeralizer(data)
        return Response(data_s.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        new_product = models.Product.objects.create(
            product_name=data["product_name"],
            product_color=data["product_color"],
            product_price=data["product_price"],
            product_availability_count=data["product_availability_count"],
            product_tax=data["product_tax"],
            product_description=data["product_description"],
            product_created_by=request.user
        )
        result = seralizers.ProductSeralizer(new_product)
        return Response(result.data)
