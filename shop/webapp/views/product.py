from typing import Any
from urllib.parse import urlencode
from django.db.models.query import QuerySet
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views import generic
from webapp.models import Product, Basket
from webapp.forms import ProductForm, SearchForm
from django.shortcuts import get_object_or_404, redirect


class ProductListView(generic.ListView):
    template_name = 'products/list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6
    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        print("Search Form Data:", self.form.data)
        print("Search Value:", self.search_value)

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(stock__gt=0).order_by('category', 'name')
        print('1', queryset)
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            print(query)
            queryset = queryset.filter(query)
            print("Filtered Queryset:", queryset)
        return queryset
    
    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductAddToBasketView(generic.View):
    def post(self, request, *args, **kwargs):
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=kwargs.get('id'))

        if product.stock >= quantity:
            basket_item, created = Basket.objects.get_or_create(product=product)

            if quantity <= product.stock and quantity > 0:
                if created:
                    basket_item.quantity = quantity
                else:
                    if basket_item.quantity + quantity <= product.stock:
                        basket_item.quantity += quantity
            else:
                pass
            

            basket_item.save()
        
        return redirect('products')
    

class ProductDetailView(generic.DetailView):
    template_name = 'products/detail.html'
    model = Product
    pk_url_kwarg = 'id'


class ProductCreateView(generic.CreateView):

    template_name = 'products/product.html'
    model = Product
    form_class = ProductForm
    extra_context = {"btn_text": "Создать"}

    def get_success_url(self):
        return reverse('products_detail', kwargs={'id': self.object.id})


class ProductUpdateView(generic.UpdateView):

    template_name = 'products/product.html'
    model = Product
    form_class = ProductForm
    pk_url_kwarg = 'id'
    extra_context = {"btn_text": "Редактировать"}

    def get_success_url(self):
        return reverse('products_detail', kwargs={'id': self.object.id})
    

class ProductDeleteView(generic.DeleteView):
    model = Product
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('products') 
    
