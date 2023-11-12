from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, TemplateView, UpdateView, DetailView
from Warehouse.forms import IncomingProductForm
from Warehouse.models import Category, Product, IncomingProduct


# Create your views here.
class CreateCategory(CreateView):
    model = Category
    template_name = "Warehouse/createcatergy.html"
    fields = "__all__"
    success_url = reverse_lazy("listcategory")


class CreateProduct(CreateView):
    model = Product
    template_name = "Warehouse/create-product.html"
    fields = "__all__"
    success_url = reverse_lazy("list")

class ListCategory(ListView):
    model = Category
    template_name = "Warehouse/listcategory.html"
    context_object_name = "Category"


class ListProduct(DetailView):
    model = Category
    template_name = "Warehouse/detailcategory.html"
    context_object_name = "products"


class IncomingProductCreate(CreateView):
    template_name = 'Warehouse/incomingproduct.html'
    form_class = IncomingProductForm
    success_url = 'list'

    def form_valid(self, form):
        products = get_object_or_404(Product, name=form.instance.product)
        products.quantity += form.instance.quantity
        products.save()
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = "home.html"
class updateproduct(UpdateView):
    model = Product
    template_name = "warehouse/update.html"
    fields = "__all__"
    success_url = reverse_lazy("list")

