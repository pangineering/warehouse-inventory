from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    username = request.user.username
    current = User.objects.get(username=username)
    context = {'data':current}
    return render(request, 'home.html', context)