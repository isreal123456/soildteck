# Generated by Django 4.2 on 2024-01-12 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Sellers", "0002_recipt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipt",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="Sellers.order",
            ),
        ),
    ]
