from django import forms
from .models import Sale, Product
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['date','product','quantity','price']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']
