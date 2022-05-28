from django.shortcuts import render

def overview(request):
    return render(request, 'buy_sell.html', {})

def buy(request):
    return render(request, 'buy.html', {})

def sell(request):
    return render(request, 'sell.html', {})

