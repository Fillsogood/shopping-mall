from rest_framework import serializers

from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer[OrderItem]):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer[OrderItem]):
    class Meta(OrderItemSerializer.Meta):
        pass
