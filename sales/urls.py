from django.urls import path
from . import views
app_name = 'sales'
urlpatterns = [
    path('', views.index, name='index'),
    path('sale/new/', views.sale_create, name='sale_create'),
    path('product/new/', views.product_create, name='product_create'),
]
