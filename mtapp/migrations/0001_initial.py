# Generated by Django 4.1.5 on 2023-02-14 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Outlet', models.CharField(max_length=30)),
                ('Outlet_Location', models.CharField(max_length=60)),
                ('Outlet_Id', models.IntegerField()),
                ('Email_address', models.EmailField(max_length=50)),
                ('Mobile_Number', models.IntegerField()),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='proupmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='mtapp/static/images')),
            ],
        ),
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
