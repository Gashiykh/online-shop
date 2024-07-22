from django import forms
from django.core import validators
from webapp.models import Product, Order


class MinInteger(validators.BaseValidator):
    message = 'value must be greater than 0'
    core = 'min_integer'

    def compare(self, value, limit):
        return value <= limit

    def clean(self, value):
        return value


class ProductForm(forms.ModelForm):
    stock = forms.IntegerField(label='Остаток', validators=[MinInteger(0)])
    class Meta:
        model = Product
        fields = ['name', 'description', 'img_url', 'category', 'stock', 'price']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="search")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['user', 'phone_number', 'address']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }