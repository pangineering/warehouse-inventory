from django.shortcuts import render

def supplier_list(request):
    return render(request, 'suppliers.html', {})

#def product_add(request):
#    return render(request, 'customer_add.html', {})

#def product_edit(request):
#    return render(request, 'customer_edit.html', {})
