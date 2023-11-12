# Generated by Django 4.2 on 2023-10-22 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Seller", "0005_rename_item_orderitem_product_remove_orderitem_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="Seller.order",
            ),
        ),
    ]
