from django.shortcuts import render, redirect
from .models import Pizza, Order
from .forms import OrderForm

def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})