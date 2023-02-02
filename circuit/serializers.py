
from rest_framework import serializers
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
        fields = ('username', 'first_name', 'last_name', 'is_active', 'password')

    def create(self, validated_data):
        staff = super().create(validated_data)
        staff.set_password(staff.password)
        print(validated_data)
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

    class Meta:
        model = InfoChain
        fields = '__all__'


class UpdateChainSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    contacts = ContactSerializer()
    products = ProductSerializer()
    debt = serializers.FloatField()

    class Meta:
        model = InfoChain
        fields = ('title', 'contacts', 'products', 'debt')

    def update(self, instance, validated_data):
        title = validated_data.pop('title')
        products_ = validated_data.pop('products')
        products = Product.objects.update(**products_)
        contacts_ = validated_data.pop('contacts')
        contacts = Contact.objects.update(**contacts_)
        debt = validated_data.pop('debt')

        instance = InfoChain.objects.update(
            title=title,
            structure=InfoChain.structure,
            products=products,
            contacts=contacts,
            debt=debt

        )
        return instance


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


class CreateChainSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    products = ProductSerializer()
    contacts = ContactSerializer()
    supplier = serializers.SlugRelatedField(slug_field='title', queryset=InfoChain.Suppler.objects.all(),
                                            allow_null=True)

    class Meta:
        model = InfoChain
        fields = ('title', 'structure', 'contacts', 'supplier', 'products', 'staff')

    def create(self, validated_data):
        title = validated_data.pop('title')
        supplier = validated_data.pop('supplier')
        staff_ = validated_data.pop('staff')
        staff = Staff.objects.create_user(**staff_)
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
        return chain
