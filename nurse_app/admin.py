from django.contrib import admin
from .models import Nurse, Order


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'experience', 'is_available']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nurse', 'client_name', 'status', 'created_at']
