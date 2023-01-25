import json
from http.client import HTTPResponse

import django_filters
import requests
from django.forms import model_to_dict
from django.http import JsonResponse
from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from circuit.models import InfoChain, Chain, Staff, Product, Contact


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active',)

    def create(self, validated_data):
        staff = super().create(validated_data)
        staff.set_password(staff.password)

        staff.save()
        return staff


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'is_active')


class InfoChainSerializer(serializers.ModelSerializer):
    staff = StaffListSerializer()
    contacts = ContactSerializer()
    supplier = ChainSerializer()
    products = ProductSerializer()

    # structure = StructureSerializer()

    class Meta:
        model = InfoChain
        fields = '__all__'


class UpdateChainSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer()

    # structure = StructureSerializer()

    class Meta:
        model = InfoChain
        fields = ('title', 'contacts', 'supplier', 'products')

    def update(self, instance, validated_data):
        title = validated_data.pop('title')
        supplier = validated_data.pop('supplier')
        products_ = validated_data.pop('products')
        products = Product.objects.update(**products_)
        contacts_ = validated_data.pop('contacts')
        contacts = Contact.objects.update(**contacts_)
        #
        chain = InfoChain.objects.update(
            title=title,
            structure=InfoChain.structure,
            supplier=supplier,
            products=products,
            contacts=contacts,

        )
        instance.save()
        return instance

    # def save(self, **kwargs):
    #     chain = super().save()
    #     chain.save()
    #     return chain


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        print(product)
        return product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain.Suppler
        fields = '__all__'


class ChainCreateSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    products = ProductSerializer()
    contacts = ContactSerializer()

    class Meta:
        model = InfoChain
        fields = ('title', 'structure', 'staff', 'contacts', 'supplier', 'products')

    def create(self, validated_data):
        title = validated_data.pop('title')
        supplier = validated_data.pop('supplier')
        staff_ = validated_data.pop('staff')
        staff = Staff.objects.create(**staff_)
        products_ = validated_data.pop('products')
        products = Product.objects.create(**products_)
        contacts_ = validated_data.pop('contacts')
        contacts = Contact.objects.create(**contacts_)

        chain = InfoChain.objects.create(
            title=title,
            structure=InfoChain.structure,
            staff=staff,
            supplier=supplier,
            products=products,
            contacts=contacts,

        )

        print(chain.structure)
        return chain
