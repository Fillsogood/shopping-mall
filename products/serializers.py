from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer[Product]):
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        pass