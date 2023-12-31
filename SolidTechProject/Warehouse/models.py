from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, help_text="eg RGB",max_length=1000000)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(blank=False, help_text="eg coke",max_length=10000000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}-{self.category.name}'


class IncomingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.product)


# Create your models here.
