from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Nurse, Order
from .forms import OrderForm, SearchNurseForm


def home(request):
    """Главная страница с формой поиска"""
    # Получаем всех доступных сиделок
    all_nurses = Nurse.objects.filter(is_available=True)

    # Показываем первых 6 на главной
    nurses = all_nurses[:6]

    # Форма поиска
    form = SearchNurseForm(request.GET or None)
    filtered_nurses = all_nurses
    has_search = False

    if request.GET and (request.GET.get('address') or request.GET.get('date') or
                        request.GET.get('time_from') or request.GET.get('time_to') or
                        request.GET.get('duration') or request.GET.get('period')):
        has_search = True
        address = request.GET.get('address', '').strip()
        date = request.GET.get('date', '').strip()
        time_from = request.GET.get('time_from', '').strip()
        time_to = request.GET.get('time_to', '').strip()
        duration = request.GET.get('duration', '').strip()
        period = request.GET.get('period', '').strip()

        # Фильтрация по адресу (поиск в специализации и описании)
        if address:
            filtered_nurses = filtered_nurses.filter(
                Q(specialization__icontains=address) |
                Q(description__icontains=address)
            )

        # Здесь можно добавить дополнительную фильтрацию
        # Пока просто показываем отфильтрованные результаты

        nurses = filtered_nurses[:6]

    context = {
        'nurses': nurses,
        'filtered_nurses': nurses,
        'form': form,
        'has_search': has_search,
        'total_found': filtered_nurses.count() if has_search else 0,
    }

    return render(request, 'nurse_app/home.html', context)


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