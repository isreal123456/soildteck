from . import views
from django.urls import path

from .views import IncomingProductCreate, ListProduct, ListCategory, HomePageView, CreateCategory, updateproduct, \
    CreateProduct

urlpatterns = [
    path('create/', IncomingProductCreate.as_view(), name='incoming'),
    path('list/<int:pk>', ListProduct.as_view(), name='list'),
    path("list2/", ListCategory.as_view(), name='listcategory'),
    path("home1/", HomePageView.as_view(), name='home'),
    path('create1', CreateCategory.as_view(), name="createcategory"),
    path("<int:pk>/product", updateproduct.as_view(), name="updateproduct"),
    path("create1/", CreateProduct.as_view(), name='createproduct')

]
