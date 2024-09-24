from django.db import models

from apps.base.models import BaseModel
from apps.users.models import User


class Address(BaseModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
