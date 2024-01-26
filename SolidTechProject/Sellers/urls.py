from . import views
from django.urls import path

from Sellers.views import CreateOrder, OrderDetail, UpdateOrder

urlpatterns = [
    path("create/order", CreateOrder.as_view(), name="createorder"),
    path('search/orders',views.search_order_by_date,name='searchorders'),
    path('add/orderitem/<int:pk>',views.add_orderitems, name='addorderitems'),
    path('order/detail/<int:pk>',OrderDetail.as_view(),name='orderdetail'),
    path("home/", views.home, name='home'),
    path('orders/',views.search_order_result,name='ordersresult'),
    path('log/',views.log,name='log'),
    path('search/log/',views.search_log_by_date,name='searchlog'),
    path('update/order/<int:pk>', UpdateOrder.as_view(), name="updateorder"),
    # path("pdf/", views.pdfgeneration.as_view(), name="pdf")
]