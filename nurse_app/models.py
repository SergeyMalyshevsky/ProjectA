from django.db import models


class Nurse(models.Model):
    EXPERIENCE_CHOICES = [
        ('1-3', '1-3 года'),
        ('3-5', '3-5 лет'),
        ('5-10', '5-10 лет'),
        ('10+', 'Более 10 лет'),
    ]

    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    experience = models.CharField('Опыт работы', max_length=10, choices=EXPERIENCE_CHOICES)
    specialization = models.CharField('Специализация', max_length=200)
    phone = models.CharField('Телефон', max_length=20)
    is_available = models.BooleanField('Доступна', default=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Сиделка'
        verbose_name_plural = 'Сиделки'

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('confirmed', 'Подтвержден'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]

    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, verbose_name='Сиделка')
    client_name = models.CharField('Имя клиента', max_length=100)
    client_phone = models.CharField('Телефон клиента', max_length=20)
    patient_name = models.CharField('Имя пациента', max_length=100)
    patient_age = models.IntegerField('Возраст пациента')
    address = models.TextField('Адрес')
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    notes = models.TextField('Дополнительная информация', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id} - {self.nurse.name}'
