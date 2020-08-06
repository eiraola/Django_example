from django.contrib import admin
from django.urls import path
from src.helloworld.views import hello
from src.products.views import home_view, contact_view, product_detail_view, product_create_view, render_initial_data,\
    dynamic_lookup_view, product_delete_view, product_list_view, product_list_view_link

app_name = 'products'
urlpatterns = [

    path('products', home_view),
    path('contacts', contact_view),
    path('product', product_detail_view),
    path('formulario', product_create_view),
    path('miformulario', render_initial_data),
    path('<int:my_id>/', dynamic_lookup_view, name='product_det'),
    path('<int:my_id>/', product_delete_view, name='product'),
    path('list', product_list_view),
    path('dlist', product_list_view_link, name='product_detail'),

]
