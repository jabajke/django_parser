from django.db import models
from parse_app.models import ParseData


class CartModel(models.Model):
    goods = models.ForeignKey(ParseData, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=0)

    def __str__(self):
        return f'Cart item for product {self.goods.title}'


class CartItem(models.Model):
    items = models.ManyToManyField(CartModel, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=0)
