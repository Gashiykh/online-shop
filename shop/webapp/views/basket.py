from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from webapp.models import Basket
from webapp.forms import OrderForm


class BasketView(generic.ListView):
    template_name = 'products/basket.html'
    model = Basket
    context_object_name = 'basket_products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        basket_products = context['basket_products']

        total = 0
        
        for item in basket_products:
            item.sum = item.product.price * item.quantity
            total += item.sum

        context['total'] = total
        context['form'] = OrderForm()

        return context
    

class DeleteFromBasketView(generic.View):
    
    def post(self, request, *args, **kwargs):
        basket_item = get_object_or_404(Basket, id=kwargs.get('id'))

        if basket_item.quantity > 1:
            basket_item.quantity -= 1
            basket_item.save()
        else:
            basket_item.delete()

        return redirect('basket')
   

   