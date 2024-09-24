from django.db import models

from common.models import CommonModel
from users.models import User


class Address(CommonModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
