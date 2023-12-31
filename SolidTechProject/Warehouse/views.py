from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, TemplateView, UpdateView, DetailView, DeleteView
from Warehouse.forms import IncomingProductForm
from Warehouse.models import Category, Product, IncomingProduct


# Create your views here.
class CreateCategory(CreateView):
    model = Category
    template_name = "Warehouse/create_category.html"
    fields = "__all__"
    success_url = reverse_lazy("listcategory")


class CreateProduct(CreateView):
    model = Product
    template_name = "Warehouse/create-product.html"
    fields = "__all__"
    success_url = reverse_lazy("listcategory")


class ListCategory(ListView):
    model = Category
    template_name = "Warehouse/list_category.html"
    context_object_name = "Category"


class ListProduct(DetailView):
    model = Category
    template_name = "Warehouse/detail_category.html"
    context_object_name = "products"


class IncomingProductCreate(CreateView):
    template_name = 'Warehouse/incoming_product.html'
    form_class = IncomingProductForm
    success_url = reverse_lazy("listcategory")

    def form_valid(self, form):
        products = get_object_or_404(Product, name=form.instance.product.name)
        products.quantity += form.instance.quantity
        products.save()
        return super().form_valid(form)

class delete(DeleteView):
    model = Product
    template_name = "Warehouse/delete.html"
    success_url = reverse_lazy("listcategory")
    context_object_name = "product"







# Create your views here.
