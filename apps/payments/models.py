from django.db import models

from apps.base.models import BaseModel
from apps.orders.models import Order


class Payment(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # 예: 'Credit Card', 'PayPal'
    is_successful = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Payment for Order {self.order.id}"
