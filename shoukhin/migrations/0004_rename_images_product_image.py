# Generated by Django 5.0.3 on 2024-04-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoukhin', '0003_rename_image_product_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]