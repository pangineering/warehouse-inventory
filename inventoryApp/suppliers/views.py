from django.shortcuts import render, redirect
from .form import SupplierForm
from .models import Suppliers
from django.contrib.auth.decorators import login_required


@login_required
def supplier_list(request):
    suppliers = Suppliers.objects.all()
    context = {'suppliers':suppliers}
    return render(request, 'suppliers.html', context)

@login_required
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

@login_required
def supplier_edit(request):
    return render(request, 'suppliers_edit.html', {})

@login_required
def supplier_info(request,pk):
    sup = Suppliers.objects.get(pk=pk)
    context = {'supplier':sup}
    return render(request, 'suppliers_info.html', context)

@login_required
def delete(request, pk):
  sup = Suppliers.objects.get(pk=pk)
  sup.delete()
  return redirect("suppliers:supplier_list")