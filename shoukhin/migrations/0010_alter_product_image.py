# Generated by Django 5.0.3 on 2024-04-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoukhin', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default_no_img.jfif', null=True, upload_to='static/images'),
        ),
    ]