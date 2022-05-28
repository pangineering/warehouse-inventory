from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('add', views.customer_add, name='customer_add'),
    path('edit', views.customer_edit, name='customer_edit')
]