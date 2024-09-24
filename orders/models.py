from django.db import models

from common.models import CommonModel
from users.models import User


class Order(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Order {self.id} by {self.user.username}"
