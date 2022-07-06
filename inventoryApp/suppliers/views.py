from django.shortcuts import render, redirect
from .form import SupplierForm
from .models import Suppliers

def supplier_list(request):
    suppliers = Suppliers.objects.all()
    context = {'suppliers':suppliers}
    return render(request, 'suppliers.html', context)

def supplier_add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SupplierForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("suppliers:supplier_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SupplierForm()
    return render(request, 'suppliers_add.html', {'form': form})

def supplier_edit(request):
    return render(request, 'suppliers_edit.html', {})
