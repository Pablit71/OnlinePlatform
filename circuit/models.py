from django.contrib.auth.models import User
from django.db import models


class Chain(models.Model):
    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"

    class Suppler(models.Model):
        CHOICES = (('plant', 'Завод'),
                   ('distributor', 'Дистрибьютор'),
                   ('dealership', 'Дилерский центр'),
                   ('large_retail_chain', 'Крупная розничная сеть'),
                   ('individual_entrepreneur', 'ИП')
                   )

    title = models.CharField(verbose_name="Название сети", max_length=255)
    structure = models.CharField(verbose_name='Структура', choices=Suppler.CHOICES, max_length=255)
    date_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.structure}'


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.CharField(verbose_name='Почта', max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    street = models.CharField(verbose_name="Улица", max_length=255)
    number_house = models.IntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email} {self.country} {self.city} {self.street} {self.number_house}'


class Staff(User):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title_product = models.CharField(verbose_name='Название Продукта', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    date = models.DateTimeField(verbose_name='Дата выхода Продукта', max_length=255)

    def __str__(self):
        return f'{self.title_product}'


class InfoChain(Chain):
    class Meta:
        verbose_name = "Информация сети"
        verbose_name_plural = "Информация сетей"

    staff = models.ForeignKey(Staff, verbose_name='Сотрудники', related_name='staff', on_delete=models.CASCADE,
                              blank=True, null=True)
    products = models.ForeignKey(Product, verbose_name='Продукты', related_name='product', on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Chain, verbose_name='Главный поставщик', on_delete=models.DO_NOTHING,
                                 related_name='suppler', blank=True, null=True)
    debt = models.FloatField(verbose_name='Задолженность', null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.debt} {self.products} {self.staff} {self.supplier}'
