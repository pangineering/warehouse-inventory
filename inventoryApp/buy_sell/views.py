from django.shortcuts import render, redirect
from .models import Purchase, Selling
from .form import PurchaseForm, OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def purchase(request):
    purchase = Purchase.objects.all()
    context = {'purchase':purchase}
    return render(request, 'purchase.html', context)


@login_required
def sell(request):
    orders = Selling.objects.all()
    context = {'orders':orders}
    return render(request, 'sell.html', context)


@login_required
def purchase_info(request,pk):
    purchase= Purchase.objects.get(pk=pk)
    context = {'purchase':purchase}
    return render(request, 'purchase_info.html', context)

@login_required
def order_info(request,pk):
    order = Selling.objects.get(pk=pk)
    context = {'order':order}
    return render(request, 'order_info.html', context)


@login_required
def add_purchase(request):
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
            return redirect("buy_sell:buy_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PurchaseForm()
    return render(request, 'add_purchase.html', {'form':form})

@login_required
def add_order(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inv = form.save(commit=False)
            inv.save()
            # ...
            # redirect to a new URL:
            return redirect("buy_sell:sell_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form':form})




@login_required
def delete_order(request, pk):
  ord = Selling.objects.get(pk=pk)
  ord.delete()
  return redirect("buy_sell:sell_list")



@login_required
def delete_purchase(request, pk):
  pur = Purchase.objects.get(pk=pk)
  pur.delete()
  return redirect("buy_sell:buy_list")

@login_required
def update_purchase(request, pk):
    inv = Purchase.objects.get(pk=pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=inv)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect("buy_sell:buy_list")
    else:
        form = PurchaseForm(instance=inv)

    return render(request,
                'edit_purchase.html',
                {'form': form})



@login_required
def update_order(request, pk):
    inv = Selling.objects.get(pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=inv)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect("buy_sell:sell_list")
    else:
        form = OrderForm(instance=inv)

    return render(request,
                'edit_order.html',
                {'form': form})