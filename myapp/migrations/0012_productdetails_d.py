# Generated by Django 3.2.5 on 2022-01-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='d',
            field=models.IntegerField(default=0),
        ),
    ]