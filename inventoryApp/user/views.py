from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Employee

@login_required
def profile(request):
    username = request.user.username
    current = User.objects.get(username=username)
    print(current.id)
    profile = Employee.objects.filter() #.filter(user=current.username)
    print(profile)
    context = {'current':current,'profile':profile}
    return render(request, 'profile.html', context)

@login_required
def setting(request):
    return render(request, 'setting.html', {})
@login_required
def register(request):
    return render(request, 'register.html', {})
