from statistics import mean

from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from circuit.models import InfoChain, Staff
from circuit.permissions import Permissions
from circuit.serializers import CreateChainSerializer, InfoChainSerializer, StaffSerializer, \
    UpdateChainSerializer


class ChainListView(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    permission_classes = [Permissions]

    def get_queryset(self):
        return InfoChain.objects.all()


class InfoChainCountry(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [Permissions]
    filterset_fields = ('contacts__country',)

    def get_queryset(self):
        return InfoChain.objects.all()


class StaticDebt(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [Permissions]

    def get_queryset(self):
        debt = []
        chain = InfoChain.objects.all()
        for i in chain:
            debt.append(i.debt)

        return InfoChain.objects.filter(debt__gt=mean(debt))


class IdProduct(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [Permissions]
    filterset_fields = ('products__id',)

    def get_queryset(self):
        return InfoChain.objects.all()


class CreateChain(APIView):
    permission_classes = [Permissions]

    def post(self, request):
        serializer = CreateChainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)


class UpdateChain(APIView):
    permission_classes = [Permissions]

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'Error': "error pk"})
        instance = InfoChain.objects.get(pk=pk)
        serializer = UpdateChainSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)


class CreateStaff(CreateAPIView):
    model = Staff
    serializer_class = StaffSerializer


class DestroyChain(DestroyAPIView):
    queryset = InfoChain.objects.all()

    def perform_destroy(self, instance: InfoChain):
        with transaction.atomic():
            instance.delete()
            instance.products.delete()
            instance.contacts.delete()
        return instance
