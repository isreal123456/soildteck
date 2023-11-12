from django.db import models
from django.urls import reverse

from Warehouse.models import Product


# Create your models here.


class Order(models.Model):
    order_id = models.CharField(unique=True, blank=False, max_length=100000000)
    # item = models.ManyToManyField(Product)
    cost = models.PositiveIntegerField(default=0)
    # open = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("list2", args=[str(self.id)])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # cost = models.PositiveIntegerField()
    def get_order(self):
        return self.order

    # def get_absolute_url(self):
    #     return reverse("createitem", args=[str(self.id)])
