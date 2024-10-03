from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager["User"]):
    def create_user(self, user_id: str, username: str, password: str) -> Any:
        if not user_id:
            raise ValueError("User ID must be provided")

        user = self.model(user_id=user_id, username=username)  # username 추가
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id: str, username: str, password: str) -> Any:
        superuser = self.create_user(user_id=user_id, username=username, password=password)  # username 추가
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, unique=True)
    nickName = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
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

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["nickName"]

    class Meta:
        db_table = "user"
