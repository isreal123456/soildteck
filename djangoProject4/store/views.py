from django.shortcuts import render
from django.views.generic import CreateView, ListView

from order.models import Order
from store.models import Item, Category


# Create your views here.
class createproduct(CreateView):
    model = Item
    template_name = "store/createproduct.html"
    fields = "__all__"

class creatcatorgy(CreateView):
    model = Category
    template_name = "store/createcategory.html"
    fields = '__all__'

class display_categories(ListView):
    model = Category
    template_name = "store/display_categories.html"

class list_order(ListView):
    model = Order
    template_name = "store/list_order.html"

