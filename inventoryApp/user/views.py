from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from .models import Employee
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from user.form import CustomUserCreationForm, ProfileForm
from django.template import RequestContext
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


@login_required
def profile(request):
    username = request.user.username
    #print(username)
    current = User.objects.get(username=username)
    print(current)
    profile = Employee.objects.filter(user=current.id)
    
    context = {'current':current,'profile':profile}
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    username = request.user.username
    current = User.objects.get(username=username)
    print(current.id)
    profile = Employee.objects.filter() #.filter(user=current.username)
    print(profile)
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.user = current
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("user:profile")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    context = {'current':current,'profile':profile,'form':form}
    return render(request, 'edit_profile.html', context)
    

@login_required
def setting(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'setting.html',{
        'form': form
    })

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
        

