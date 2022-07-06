from django.urls import path
from suppliers import views

app_name = 'suppliers'

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('add', views.supplier_add, name='supplier_add'),
    path('edit', views.supplier_edit, name='supplier_edit'),
    path('info/<int:pk>', views.supplier_info, name='supplier_info')
]