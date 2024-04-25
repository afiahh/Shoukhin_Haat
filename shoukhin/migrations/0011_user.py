# Generated by Django 5.0.3 on 2024-04-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoukhin', '0010_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('nid', models.CharField(max_length=20)),
                ('account_type', models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], max_length=10)),
                ('picture', models.ImageField(blank=True, default='static/images/default_no_img.jfif', null=True, upload_to='static/images')),
                ('about_myself', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]