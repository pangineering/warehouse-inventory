from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('setting', views.setting, name='setting'),
    path('register', views.register, name='register'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]