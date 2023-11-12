from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, help_text="eg RGB",max_length=1000000)
    description = models.TextField(blank=True, max_length=100000000000000000000)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(blank=False, help_text="eg coke",max_length=10000000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class IncomingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
