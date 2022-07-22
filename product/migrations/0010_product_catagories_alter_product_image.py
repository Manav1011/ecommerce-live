# Generated by Django 4.0.5 on 2022-07-22 13:22

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagories',
            field=models.CharField(choices=[('wearable', 'Wearable'), ('digital', 'Digital')], default='wearable', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
    ]