from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy, reverse

from Warehouse.models import Product

Status = (
    ("Paid", "Paid"),
    ("Completed", "Completed"),
)

user = get_user_model()


class Log(models.Model):
    log = models.CharField(max_length=10000000)
    date_created = models.DateTimeField(auto_now_add=True)

    date = models.DateField(null=True, blank=True, auto_now_add=True)


class Order(models.Model):
    seller = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=1000000)
    num_of_product = models.IntegerField(max_length=100000)
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, )
    status = models.CharField(max_length=200, choices=Status, default="COMPLETED BUT NOT PAID", blank=True, null=True)
    serial_num = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    @property
    def get_order_items(self):
        orderItems = OrderItem.objects.filter(order_id=self.pk)
        return orderItems

    @property
    def total_price(self):
        order_items = OrderItem.objects.filter(order_id=self.id)
        cost = 0
        for order_item in order_items:
            cost += order_item.cost
        return cost


class OrderItem(models.Model):
    seller = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{(self.order)} - {self.item}'

    @property
    def cost(self):
        return self.item.price * self.quantity

    def get_order_items(self):
        orderItems = OrderItem.objects.filter(order_id=self.pk)
        return orderItems


# class Payment(models.Model):
#     seller = models.ForeignKey(user, on_delete=models.DO_NOTHING)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#     status = models.CharField(max_length=200, choices=Status, blank=True, null=True)
#     created_at = models.DateField(auto_now_add=True, null=True)
#
#     @property
#     def get_order_items(self):
#         orderItems = OrderItem.objects.filter(order_id=self.pk)
#         return orderItems
#
#     @property
#     def total_price(self):
#         order_items = OrderItem.objects.filter(order_id=self.id)
#         cost = 0
#         for order_item in order_items:
#             cost += order_item.cost
#         return cost
#
#     @property
#     def cost(self):
#         return self.item.price * self.item.quantity
#
#     def get_order_items(self):
#         orderItems = OrderItem.objects.filter(order_id=self.pk)
#         return orderItems
#
# # Create your models here.
