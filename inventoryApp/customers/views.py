from django.shortcuts import render

def customer_list(request):
    return render(request, 'customers.html', {})

def customer_add(request):
    return render(request, 'customer_add.html', {})

def customer_edit(request):
    return render(request, 'customer_edit.html', {})
