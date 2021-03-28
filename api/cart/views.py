from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from . import models
from . import seralizers

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated,])
def userCartExists(request):
    if request.method == "GET":
        try:
            data = models.Cart.objects.filter(current_user_id=request.user.id)
            data_seralizer = seralizers.CartSeralizer(data, many=True)
            if len(data_seralizer.data) == 1:
                return JsonResponse({"isExists": True}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"isExists": False}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({"message": "BAD REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST":
        seralizer = seralizers.CartSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated,])
def userCartModifications(request):
    try:
        cart = models.Cart.objects.filter(current_user_id=request.user.id)
    except models.Cart.DoesNotExist:
        return Response({"error": {"error": 404, "message": "Cart Object not found!"}}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        seralizer = seralizers.CartSeralizer(cart, many=True)
        return Response(seralizer.data)
    elif request.method == "PUT":
        seralizer = seralizers.CartSeralizer(cart, data=request.data, many=True)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserCart(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = seralizers.CartSeralizer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        pass

    def list(self, request, *args, **kwargs):
        data = models.Cart.objects.filter(current_user_id=request.user.id)
        data_seralizer = seralizers.CartSeralizer(data, many=True)
        return Response(data_seralizer.data)

    # def list(self, request, *args, **kwargs):
    #     print(request.user)
    #     data = models.Cart.objects.all()
    #     data_s = seralizers.CartSeralizer(data)
    #     return Response(data_s.data)

class UserCartProducts(viewsets.ModelViewSet):
    queryset = models.CartProducts.objects.all()
    serializer_class = seralizers.CartProductSeralizer
    permission_classes = (IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        get_cart_id = models.Cart.objects.filter(current_user_id=request.user.id)
        cart_id_seralizer = seralizers.CartSeralizer(get_cart_id, many=True)
        data = models.CartProducts.objects.filter(cart_id=cart_id_seralizer.data[0]["current_user_id"])
        data_S = seralizers.CartProductSeralizer(data, many=True)
        return Response(data_S.data)