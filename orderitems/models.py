from django.db import models

from common.models import CommonModel
from orders.models import Order
from products.models import Product


class OrderItem(CommonModel):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name}"
