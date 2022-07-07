from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inventory
from django.http import HttpResponseRedirect
from .form import InventoryForm


@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {'inventories':inventories}
    return render(request, 'inventory_list.html', context)

@login_required
def inventory_edit(request):
    return render(request, 'inventory_edit.html', {})

@login_required
def inventory_info(request,pk):
    inv = Inventory.objects.get(pk=pk)
    context = {'inventory':inv}
    return render(request, 'inventory_info.html', context)


@login_required
def inventory_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InventoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("inventory:inventory_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InventoryForm()
    return render(request, 'inventory_add.html', {'form': form})


@login_required
def delete(request, pk):
  inv = Inventory.objects.get(pk=pk)
  inv.delete()
  return redirect("inventory:inventory_list")