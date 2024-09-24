from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager["User"]):

    def create_user(self, email: str, username: str, password: str, phone_number: str) -> Any:
        if not email:
            raise ValueError("User ID must be provided")

        user = self.model(email=email, username=username, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, username: str, password: str, phone_number: str) -> Any:
        superuser = self.create_user(
            email=email,
            username=username,
            password=password,
            phone_number=phone_number,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    nickName = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)  # 유저 ID
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # 전화번호

    is_seller = models.BooleanField(default=False)  # 판매자 여부
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)  # 프로필 사진

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickName"]

    class Meta:
        db_table = "user"
