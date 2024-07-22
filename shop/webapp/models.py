from django.db import models


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
    

class Basket(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='baskets', on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    

class Order(models.Model):
    user = models.CharField(max_length=100, verbose_name="Имя пользователя")
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    def __str__(self) -> str:
        return f'{self.id} - {self.user}'
    

class OrderProduct(models.Model):
    order = models.ForeignKey("webapp.Order", on_delete=models.CASCADE, related_name='product_orders', verbose_name="Заказ")
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="order_products", verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'