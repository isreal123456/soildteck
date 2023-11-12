# from random import randint
#
# from django.shortcuts import redirect
# from django.views.generic import CreateView
#
# from Seller.models import Order
#
# def randname():
#     while True:
#         no = f"order#{randint(1,1234342898274928)}"
#         order = Order.objects.all()
#         if no != order.order_id:
#             break
#     return no
# class createorder(CreateView):
#     model = Order
#     template_name = "seller/createorder.html"
#
#
# def createorder(request):
#     Order.objects.create(order_id=randname())
#     return redirect('listcart')
