from django.contrib import admin
from webapp.models import Product, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'created_at')
    ordering = ('-created_at',)


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)