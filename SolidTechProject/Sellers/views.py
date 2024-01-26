from django.utils.timezone import localtime, localdate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.forms import formset_factory, inlineformset_factory
from Sellers.forms import OrderItemForm, OrderForm, OrderItemFormset
from Sellers.models import Order, OrderItem
from Warehouse.models import Product
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A8


def pdf(request):
    buf = io.BytesIO()
    cavas =canvas.Canvas(buf, pagesize=A8, bottomup=0)
class CreateOrder(CreateView):
    template_name = "seller/create_order.html"
    form_class = OrderForm

    def get_success_url(self):
        return reverse_lazy('addorderitems', kwargs={'pk': self.object.pk})


def search_order_by_date(request):
    return render(request, 'seller/search_orders.html')


class OrderDetail(DetailView):
    model = Order
    template_name = 'seller/detail_order.html'


def add_orderitems(request, pk):
    context = {}
    obj = get_object_or_404(Order, pk=pk)
    orderItemFormset = inlineformset_factory(Order,OrderItem,fields=('item','quantity',),extra=obj.num_of_product)

    if request.method == 'POST':
        orderItems = orderItemFormset(request.POST,instance=obj)

        if orderItems.is_valid():
            items = orderItems.save(commit=False)
            for orderItem in items:
                id = orderItem.item.pk
                product = get_object_or_404(Product, pk=id)
                if orderItem.quantity <= product.quantity:
                    product.quantity -= orderItem.quantity
                    product.save()
                    orderItem.save()
                    obj.completed = True
                    obj.save()

                else:
                    messages.error(request,f"We don't Currently have the quantity available for {orderItem.item}")
    if obj == True:
        return redirect('orderdetail', pk=pk)
    context['formset'] = orderItemFormset
    context['obj'] = obj
    return render(request, "seller/add_orderitems.html", context)


def home(request, since=None):
    orders = Order.objects.filter(created_at__day=localdate().today().day,completed=True)
    cost = 0
    for order in orders:
        cost += order.total_price
    order = Order.objects.filter(created_at__day=localdate().today().day,completed=True).count()
    last_five_orders = Order.objects.filter(completed=True).order_by('-id')[:5]
    context = {'cost':cost,'order':order,'last_five_orders':last_five_orders}
    return render(request,'home.html',context)


def search_order_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        orders = Order.objects.filter(created_at=searched,completed=True).order_by('-id')
        if searched is False:
            messages.error(request, f"You must input a date")
        else:
            context = {
                'searched': searched,
                'orders': orders,
            }
            return render(request, 'seller/order_result.html', context)
    else:
        return render(request, 'seller/order_result.html', {})