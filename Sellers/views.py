from datetime import datetime

from django.http import HttpResponse
from django.utils.timezone import localtime, localdate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.forms import formset_factory, inlineformset_factory
from Sellers.forms import OrderItemForm, OrderForm, OrderItemFormset, UpdateOrderForm
from Sellers.models import Order, OrderItem, Log
from Sellers.utils import reder
from Warehouse.models import Product


def log(request):
    if request.method == "POST":
        searched = request.POST['searched']
        print(str(searched))
        log = Log.objects.filter(date=searched).order_by('-id')

        context = {
            'searched': searched,
            'log': log,
        }
        return render(request, 'seller/log.html', context)
    else:
        return render(request, 'seller/log.html', {})


def search_log_by_date(request):
    return render(request, 'seller/search_log.html')


class CreateOrder(CreateView):
    template_name = "seller/create_order.html"
    form_class = OrderForm

    def get_success_url(self):
        return reverse_lazy('addorderitems', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.status = 'PENDING'
        form.instance.seller = self.request.user
        var = Order.objects.order_by("-pk")[0]
        form.instance.serial_num = var.serial_num + 1
        form.save()
        return super().form_valid(form)


def search_order_by_date(request):
    return render(request, 'seller/search_orders.html')


class OrderDetail(DetailView):
    model = Order
    template_name = 'seller/detail_order.html'
    context_object_name = 'order'


def add_orderitems(request, pk):
    context = {}
    obj = get_object_or_404(Order, pk=pk)
    orderItemFormset = inlineformset_factory(Order, OrderItem, fields=('item', 'quantity',), extra=obj.num_of_product)

    if request.method == 'POST':
        orderItems = orderItemFormset(request.POST, instance=obj)

        if orderItems.is_valid():
            items = orderItems.save(commit=False)
            completed = False

            for orderItem in items:
                id = orderItem.item.pk
                product = get_object_or_404(Product, pk=id)
                if orderItem.quantity > product.quantity:
                    completed = False
                    messages.error(request, f"We don't Currently have the quantity available for {orderItem.item}")

            count = 0

            if not completed:
                for item in items:
                    id = item.item.pk
                    product = get_object_or_404(Product, pk=id)
                    product.quantity -= item.quantity
                    product.save()
                    completed = False
                    item.seller = request.user

                    count += 1

                    if count == len(items):
                        obj.completed = False
                        obj.status = 'PENDING'
                        obj.save()
                    item.save()
                    if product.quantity == 0:
                        product.availability = False
                        product.save()

            if not completed:
                return redirect('orderdetail', pk=pk)

    context['formset'] = orderItemFormset
    context['obj'] = obj

    return render(request, "seller/add_orderitems.html", context)


def home(request, since=None):
    orders = Order.objects.filter(created_at__day=localdate().today().day, completed=False)
    cost = 0
    for order in orders:
        cost += order.total_price
    order = Order.objects.filter(created_at__day=localdate().today().day, completed=False).count()
    last_five_orders = Order.objects.filter(created_at=localdate().today(), completed=False).order_by('-id')[:5]
    context = {'cost': cost, 'order': order, 'last_five_orders': last_five_orders, 'orders_made': orders}
    return render(request, 'home.html', context)


def search_order_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        orders = Order.objects.filter(created_at=searched, completed=False).order_by('-id')

        context = {
            'searched': searched,
            'orders': orders,
        }
        return render(request, 'seller/order_result.html', context)
    else:
        return render(request, 'seller/order_result.html', {})


# class CreatePayment(CreateView):
#     form_class = PaymentForm
#     template_name = "seller/update_order.html"
#
#     def get_success_url(self):
#         return reverse_lazy('orderdetail', kwargs={'pk': self.object.pk})
#
#
#     def get_order(self):
#         order = Order.objects.filter()

class UpdateOrder(UpdateView):
    model = Order
    fields = ["status"]
    template_name = 'seller/update_order.html'
    context_object_name = "update"


    # def get_queryset(self):
    #     return UpdateOrder.form_class.fields==

    # def form_valid(self, form):
    # #     messages.success(self.request, "The payment was successful")
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('orderdetail', kwargs={'pk': self.object.pk})


# class pdfgeneration(View):
#     def get(self, request, *args, **kwargs):
#         pdf = reder("detail_order.html")
#         return HttpResponse(pdf, content_type='application/pdf')
