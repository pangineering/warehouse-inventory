from django.shortcuts import render, redirect
from .models import Purchase, Selling
from .form import PurchaseForm


def purchase(request):
    purchase = Purchase.objects.all()
    context = {'purchase':purchase}
    return render(request, 'purchase.html', context)



def sell(request):
    return render(request, 'sell.html', {})

def add_order(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PurchaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.employee_number = "0000"
            inv.user = request.user
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("inventory:inventory_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PurchaseForm()
    return render(request, 'add_order.html', {'form':form})

