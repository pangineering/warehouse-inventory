from django.urls import path
from buy_sell import views

app_name = 'buy_sell'

urlpatterns = [
    path('sell', views.sell, name='sell_list'),
    path('buy', views.purchase, name='buy_list'),
    path('add_purchase',views.add_purchase,name='add_purchase'),
    path('add_order',views.add_order,name='add_order'),
    path('info-purchase/<int:pk>', views.purchase_info, name='purchase_info'),
    path('info-order/<int:pk>', views.order_info, name='order_info'),
    path('delete/order/<int:pk>', views.delete_order, name='delete_order'),
    path('delete/purchase/<int:pk>', views.delete_purchase, name='delete_purchase'),
    path('edit-purchase/<int:pk>', views.update_purchase, name='purchase_edit'),
    path('edit-order/<int:pk>', views.update_order, name='order_edit')
]
