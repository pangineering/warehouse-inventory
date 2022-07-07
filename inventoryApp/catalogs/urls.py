from django.urls import path
from catalogs import views

app_name = 'catalogs'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add', views.product_add, name='product_add'),
    path('edit', views.product_edit, name='product_edit'),
    path('info/<int:pk>', views.product_info, name='product_info'),
    path('delete/<int:pk>', views.delete, name='delete')
]