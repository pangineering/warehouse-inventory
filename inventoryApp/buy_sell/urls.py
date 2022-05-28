from django.urls import path
from buy_sell import views

app_name = 'buy_sell'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('sell', views.sell, name='sell_list'),
    path('buy', views.buy, name='buy_list')
]