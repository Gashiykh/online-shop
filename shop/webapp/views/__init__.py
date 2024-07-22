from webapp.views.product import (
    ProductListView,
    ProductDetailView,
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView,
    ProductAddToBasketView,
    )
from webapp.views.basket import(
    BasketView,
    DeleteFromBasketView,
)
from webapp.views.order import(
    CreateOrderView
)

from django.views import generic


class IndexRedirectView(generic.RedirectView):
    pattern_name = 'products'