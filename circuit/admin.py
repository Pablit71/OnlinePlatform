from django.contrib import admin

from circuit.models import BaseModel, Structures, Product, Contact, Address, Chain


# Register your models here.
@admin.register(BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contacts', 'products', 'staff', 'suppler', 'debt', 'date_creation')
    list_display_links = ('title',)
    search_fields = ('title', 'id')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city', 'street', 'number_house')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'date')


@admin.register(Structures)
class StructuresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'structure')
