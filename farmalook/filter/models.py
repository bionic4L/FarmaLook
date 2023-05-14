from django.db import models
from django import forms

class Table(models.Model):
    """Класс создания модели таблицы"""
    company_name = models.CharField(max_length=250, verbose_name='Название компании')
    reg_date = models.DateField(
        editable=True,
        verbose_name='Дата создания',
    )
    country_company = models.CharField(max_length=50, verbose_name='Страна заказчика')
    aid_form = models.CharField(max_length=500, verbose_name='Форма препарата')
    aid_name = models.CharField(max_length=100, verbose_name='Название препарата')
    mnn = models.CharField(max_length=100, verbose_name='Международное непатентованное наименование')
    dru = models.CharField(max_length=200, verbose_name='Держатель регистрационного удостоверения')
