from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Order, Deliverer
from .forms import OrderForm, DelivererForm, AssignDelivererForm

def index(request):
    return render(request, 'home.html')

def make_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'make_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def assign_deliverer(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = AssignDelivererForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = AssignDelivererForm(instance=order)
    return render(request, 'assign_deliverer.html', {'form': form, 'order': order})
