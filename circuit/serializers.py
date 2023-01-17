from rest_framework import serializers

from circuit.models import BaseModel, Product, Contact, Structures, Chain, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = '__all__'


class StructuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structures
        fields = '__all__'


class ChainSerializer(serializers.ModelSerializer):
    structure = StructuresSerializer()

    class Meta:
        model = Chain
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BaseModelSerializer(serializers.ModelSerializer):
    products = ProductSerializer()
    contacts = ContactSerializer()
    suppler = ChainSerializer()

    class Meta:
        model = BaseModel
        fields = '__all__'
