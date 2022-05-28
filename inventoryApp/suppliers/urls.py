from django.urls import path
from suppliers import views

app_name = 'suppliers'

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    #path('add', views.customer_add, name='customer_add'),
    #path('edit', views.customer_edit, name='customer_edit')
]