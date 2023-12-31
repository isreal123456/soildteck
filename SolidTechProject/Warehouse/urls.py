from . import views
from django.urls import path

from .views import IncomingProductCreate, ListProduct, ListCategory, CreateCategory, \
    CreateProduct, delete

urlpatterns = [
    path('create/incoming/product', IncomingProductCreate.as_view(), name='incoming'),
    path('list/product/<int:pk>', ListProduct.as_view(), name='list'),
    path("list/category", ListCategory.as_view(), name='listcategory'),
    path('delete/<int:pk>', delete.as_view(), name='delete'),
    path('create/category', CreateCategory.as_view(), name="createcategory"),
    path("create/product", CreateProduct.as_view(), name='createproduct')

]