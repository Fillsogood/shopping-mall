from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer[Order]):
    class Meta:
        model = Order
        fields = "__all__"

    def validate_total_amount(self, value: int) -> int:
        if value < 0:
            raise serializers.ValidationError("총 금액은 0 이상이어야 합니다.")
        return value


class OrderDetailSerializer(serializers.ModelSerializer[Order]):
    class Meta(OrderSerializer.Meta):
        pass
