# Generated by Django 3.2.25 on 2024-07-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание товара')),
                ('img_url', models.URLField(verbose_name='Фото товара')),
                ('category', models.CharField(choices=[('food', 'Еда'), ('drink', 'Напитки'), ('electronics', 'Электроника'), ('other', 'Другое')], default='other', max_length=50, verbose_name='Категория')),
                ('stock', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
        ),
    ]
