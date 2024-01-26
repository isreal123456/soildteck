from . import views
from django.urls import path

from Sellers.views import CreateOrder,  OrderDetail

urlpatterns = [
    path("create/order", CreateOrder.as_view(), name="createorder"),
    path('search/orders',views.search_order_by_date,name='searchorders'),
    path('add/orderitem/<int:pk>',views.add_orderitems, name='addorderitems'),
    path('order/detail/<int:pk>',OrderDetail.as_view(),name='orderdetail'),
    path("home/", views.home, name='home'),
    path("pdf", views.pdf, name='pdf'),
    path('orders/',views.search_order_result,name='ordersresult')
]