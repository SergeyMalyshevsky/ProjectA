from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Nurse, Order
from .forms import OrderForm


def home(request):
    nurses = Nurse.objects.filter(is_available=True)[:6]
    return render(request, 'nurse_app/home.html', {'nurses': nurses})


def nurse_list(request):
    nurses = Nurse.objects.filter(is_available=True)
    return render(request, 'nurse_app/nurse_list.html', {'nurses': nurses})


def nurse_detail(request, nurse_id):
    nurse = get_object_or_404(Nurse, id=nurse_id)
    return render(request, 'nurse_app/nurse_detail.html', {'nurse': nurse})


def create_order(request, nurse_id):
    nurse = get_object_or_404(Nurse, id=nurse_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.nurse = nurse
            order.save()
            messages.success(request, f'Заказ №{order.id} успешно создан!')
            return redirect('nurse_app:home')
    else:
        form = OrderForm()

    return render(request, 'nurse_app/order_form.html', {
        'form': form,
        'nurse': nurse
    })