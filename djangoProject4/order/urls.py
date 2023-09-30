from django.urls import path
from . import views

urlpatterns=[
    path('order/create',views.createorder,name='order_create')
]