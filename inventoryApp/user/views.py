from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Employee
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from user.form import CustomUserCreationForm
from django.template import RequestContext

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


def register(request):
    if request.method == "GET":
        return render(
            request, "../templates/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        else:
            return redirect("login")
        

