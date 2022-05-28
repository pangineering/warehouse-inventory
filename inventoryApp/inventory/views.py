from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Inventory

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {'inventories':inventories}
    return render(request, 'inventory_list.html', context)

@login_required
def inventory_add(request):
    return render(request, 'inventory_add.html', {})
    
@login_required
def inventory_edit(request):
    return render(request, 'inventory_edit.html', {})