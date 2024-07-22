from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from webapp.models import OrderProduct, Order, Basket
from webapp.forms import OrderForm


class CreateOrderView(generic.CreateView):
    model = Order 
    form_class = OrderForm
    template_name = 'products/basket.html'
    extra_context = {"btn_text": "Оформить заказ"}

    def form_valid(self, form: BaseModelForm):
        response = super().form_valid(form)

        basket_product = Basket.objects.all()

        for item in basket_product:
            OrderProduct.objects.create(order=self.object, product=item.product, quantity=item.quantity)
            item.product.stock -= item.quantity
            item.product.save()

        Basket.objects.all().delete()

        return response
    
    def get_success_url(self):
        return reverse('products')