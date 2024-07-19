from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY = [
        ('food', 'Еда'),
        ('drink', 'Напитки'),
        ('electronics', 'Электроника'),
        ('other', 'Другое'),
    ]
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="Описание товара")
    img_url = models.URLField(verbose_name="Фото товара")
    category = models.CharField(max_length=50, choices=CATEGORY, default='other', verbose_name='Категория')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.name