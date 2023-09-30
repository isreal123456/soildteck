from random import random, randint

from django.shortcuts import render
from django.views.generic import CreateView

from order.forms import OrderForm
from order.models import Order


# Create your views here.
# class createorder(CreateView):
#     model = Order
#     template_name = "order/createorder.html"
#     fields = "__all__"
#     queryset = Order
#
#     def form_valid(self, form):
#         if not Order.ob.get(name="order_id"):
#             ran = randint(1,23878754576787)
#             form.intance.order_id.

def createorder(request):
    form=OrderForm()
    if request.method == 'POST':
        form=OrderForm(request.POST)

        orders = Order.objects.filter(open_status=True)

        if form.is_valid():
            order=form.save(commit=False)
            for ord in orders:
                ord.open_status = False
                ord.close_status = True
                ord.save()
            order.order_id = randint(1,23878754576787)

            order.save()

    return render(request, "order.html", {'form': form})

