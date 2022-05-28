from django.shortcuts import render

def product_list(request):
    return render(request, 'catalogs.html', {})

#def product_add(request):
#    return render(request, 'customer_add.html', {})

#def cproduct_edit(request):
#    return render(request, 'customer_edit.html', {})
