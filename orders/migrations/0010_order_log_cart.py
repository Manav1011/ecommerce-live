# Generated by Django 4.0.5 on 2022-07-26 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_order_log_cart_alter_order_log_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_log',
            name='cart',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
