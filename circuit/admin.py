from django.contrib import admin
from django.db.models import QuerySet

from circuit.models import InfoChain, Product, Contact, Staff


# Register your models here.

@admin.register(InfoChain)
class InfoChain(admin.ModelAdmin):
    list_display = ('id', 'title', 'products', 'supplier', 'debt', 'date_creation')
    list_display_links = ('supplier', 'title')
    list_filter = ('contacts__city',)
    actions = ['cancellation']

    @admin.action(description='Аннулировать задолженость')
    def cancellation(self, requests, q: QuerySet):
        q.update(debt=0)


@admin.register(Staff)
class Staff(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active',)
    list_display_links = ('id', 'first_name', 'last_name', 'is_active')
    exclude = ('password', 'groups', 'user_permissions', 'date_joined', 'email', 'last_login')


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title_product', 'model', 'date')
    list_display_links = ('id', 'title_product', 'model', 'date')


@admin.register(Contact)
class Product(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'number_house')
