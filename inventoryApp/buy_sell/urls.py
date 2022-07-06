from django.urls import path
from buy_sell import views

app_name = 'buy_sell'

urlpatterns = [
    path('sell', views.sell, name='sell_list'),
    path('buy', views.purchase, name='buy_list'),
    path('add_purchase',views.add_purchase,name='add_purchase'),
    path('add_order',views.add_order,name='add_order'),
    path('info-purchase/<int:pk>', views.purchase_info, name='purchase_info'),
    path('info-order/<int:pk>', views.order_info, name='order_info')
]
