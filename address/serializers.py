from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta(AddressSerializer.Meta):
        pass
