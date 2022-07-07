from itertools import product
from django.shortcuts import render, redirect
from .models import Products
from .form import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'catalogs.html', context)

@login_required
def product_add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("catalogs:product_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()
   
    return render(request, 'add_product.html', {'form': form})
    
@login_required
def product_edit(request):
    return render(request, 'edit_product.html', {})

@login_required
def product_info(request,pk):
    inv = Products.objects.get(pk=pk)
    context = {'inventory':inv}
    return render(request, 'inventory_info.html', context)


@login_required
def delete(request, pk):
  cus = Products.objects.get(pk=pk)
  cus.delete()
  return redirect("customers:customer_list")