from django.urls import path
from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add', views.inventory_add, name='inventory_add'),
    path('edit/<int:pk>', views.update, name='inventory_edit'),
    path('info/<int:pk>', views.inventory_info, name='inventory_info'),
    path('delete/<int:pk>', views.delete, name='delete')
]