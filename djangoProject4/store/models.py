from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField("/image")
    category = models.ForeignKey(Category, models.CASCADE)
    price = models.FloatField()
    description = models.TextField(blank=True)
    quantity_on_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
