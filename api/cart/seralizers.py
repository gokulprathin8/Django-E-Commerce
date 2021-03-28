from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CartSeralizer(serializers.ModelSerializer):
    # current_user_id = UserSerializer(many=True)

    class Meta:
        model = models.Cart
        read_only_fields = ('id',)
        fields = ('current_user_id', 'created_at', 'updated_at')

class CartProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProducts
        fields = '__all__'
        depth = 1