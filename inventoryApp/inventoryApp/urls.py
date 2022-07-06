from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('dashboard.urls')),
    path('inventory/', include('inventory.urls')),
    path('', include('inventory.urls')),
    path('user/', include('user.urls')),
    path('customers/', include('customers.urls')),
    path('orders/', include('buy_sell.urls')),
   # path('reports/', include('reports.urls')),
    path('catalogs/', include('catalogs.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'),name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout')
]
