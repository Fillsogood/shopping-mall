from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer[Address]):
    class Meta:
        model = Address
        fields = "__all__"


class AddressDetailSerializer(serializers.ModelSerializer[Address]):
    class Meta(AddressSerializer.Meta):
        pass
