from django.shortcuts import render, redirect
from .form import CustomerForm
from .models import Customers

def customer_list(request):
    customers = Customers.objects.all()
    context = {'customers':customers}
    return render(request, 'customers.html', context)

def customer_add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("customers:customer_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})

def customer_edit(request):
    return render(request, 'customer_edit.html', {})
