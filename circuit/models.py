from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    street = models.CharField(verbose_name="Улица", max_length=255)
    number_house = models.CharField(verbose_name="Номер дома", max_length=255)


class Contact(models.Model):
    email = models.CharField(verbose_name='Почта', max_length=255)
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.CASCADE)


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    date = models.DateTimeField(verbose_name='Дата выхода')


class Structures(models.Model):
    title = models.CharField(verbose_name='Структура', max_length=255)


class Chain(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    structure = models.ForeignKey(Structures, verbose_name='Структура', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"



class BaseModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    contacts = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, verbose_name="Продукты", on_delete=models.CASCADE)
    staff = models.TextField(verbose_name='Сотрудники', max_length=4000)
    suppler = models.ForeignKey(Chain, verbose_name='Поставщик', on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name='Задолженность')
    date_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
