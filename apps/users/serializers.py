from typing import Any, Dict

from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSignupSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ("nickName", "username", "email", "password", "phone_number")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "nickName": {"required": True},
        }

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_email(self, email: str) -> str:
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("이메일이 이미 존재합니다.")
        return email

    def validate_nickName(self, nickName: str) -> str:
        if User.objects.filter(nickName=nickName).exists():
            raise serializers.ValidationError("닉네임이 이미 존재합니다.")
        return nickName


class UserDetailSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["id", "username", "email", "nickName", "phone_number"]  # 수정 가능한 필드만 포함
        extra_kwargs = {"password": {"write_only": True}}  # 비밀번호는 쓰기 전용

    def update(self, instance: User, validated_data: Dict[str, Any]) -> User:
        password = validated_data.pop("password", None)  # 비밀번호가 포함되어 있으면 분리
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # 비밀번호 해싱
        instance.save()
        return instance
