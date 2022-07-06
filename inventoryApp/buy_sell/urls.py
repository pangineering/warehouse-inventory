from django.urls import path
from buy_sell import views

app_name = 'buy_sell'

urlpatterns = [
    path('sell', views.sell, name='sell_list'),
    path('buy', views.purchase, name='buy_list'),
    path('add_purchase',views.add_purchase,name='add_purchase'),
    path('add_order',views.add_order,name='add_order')
    
]
