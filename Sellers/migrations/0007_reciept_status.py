# Generated by Django 5.0.1 on 2024-01-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sellers', '0006_reciept_delete_recipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciept',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Not paided', 'Not paided'), ('Paided', 'paided')], default=1, max_length=20),
        ),
    ]
