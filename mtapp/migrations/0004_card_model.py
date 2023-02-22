# Generated by Django 4.1.5 on 2023-02-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtapp', '0003_remove_buy_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder_name', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('date', models.CharField(max_length=60)),
                ('security_code', models.IntegerField()),
            ],
        ),
    ]