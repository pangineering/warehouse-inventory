from django.urls import path
from catalogs import views

app_name = 'catalogs'

urlpatterns = [
    path('product', views.product_list, name='product_list'),
    path('product/add', views.product_add, name='product_add'),
    path('product/edit/<str:pk>', views.product_edit, name='product_edit'),
    path('product/delete/<str:pk>', views.delete_product, name='delete_product'),
    path('product/info/<str:pk>', views.product_info, name='product_info'),
]