from django.urls import path
from catalogs import views

app_name = 'catalogs'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    #path('add', views.customer_add, name='customer_add'),
    #path('edit', views.customer_edit, name='customer_edit')
]