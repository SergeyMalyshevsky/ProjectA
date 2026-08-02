from django.urls import path
from . import views

app_name = 'nurse_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('nurses/', views.nurse_list, name='nurse_list'),
    path('nurse/<int:nurse_id>/', views.nurse_detail, name='nurse_detail'),
    path('order/<int:nurse_id>/', views.create_order, name='create_order'),
]