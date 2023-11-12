from django import forms
from Seller.models import OrderItem, Order


class item(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'


class order(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
