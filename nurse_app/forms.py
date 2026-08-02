from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client_name', 'client_phone', 'patient_name',
                  'patient_age', 'address', 'start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SearchNurseForm(forms.Form):
    """Форма для поиска и фильтрации сиделок"""
    PERIOD_CHOICES = [
        ('', 'Не важно'),
        ('one_time', 'Разово'),
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    DURATION_CHOICES = [
        ('', 'Не важно'),
        ('1-3', '1-3 часа'),
        ('3-6', '3-6 часов'),
        ('6-12', '6-12 часов'),
        ('12-24', '12-24 часа'),
        ('1-3_days', '1-3 дня'),
        ('3-7_days', '3-7 дней'),
        ('7-14_days', '7-14 дней'),
        ('14+_days', 'Более 14 дней'),
    ]

    address = forms.CharField(
        label='Адрес',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите адрес, где нужна сиделка (город, улица, район)',
            'class': 'search-input',
            'style': 'width: 100%;'
        })
    )

    date = forms.DateField(
        label='Дата',
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'search-input'
        })
    )

    time_from = forms.TimeField(
        label='Время от',
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'search-input'
        })
    )

    time_to = forms.TimeField(
        label='Время до',
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'search-input'
        })
    )

    duration = forms.ChoiceField(
        label='Продолжительность',
        choices=DURATION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'search-select'})
    )

    period = forms.ChoiceField(
        label='Периодичность',
        choices=PERIOD_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'search-select'})
    )