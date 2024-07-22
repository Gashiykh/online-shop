"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexRedirectView.as_view(), name='redirect'),
    path('products', views.ProductListView.as_view(), name='products'),
    path('products/create', views.ProductCreateView.as_view(), name='products_create'),
    path('products/<int:id>', views.ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:id>/add_to_basket', views.ProductAddToBasketView.as_view(), name='add_to_basket'),
    path('products/<int:id>/update', views.ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:id>/delete', views.ProductDeleteView.as_view(), name='products_delete'),
    path('basket', views.BasketView.as_view(), name='basket'),
    path('basket/delete/<int:id>', views.DeleteFromBasketView.as_view(), name='baskets_delete'),
    path('order/create', views.CreateOrderView.as_view(), name='orders_create'),
    
]
