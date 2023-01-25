from statistics import mean

from django.http import JsonResponse
from django.shortcuts import render
from django_filters import FilterSet, AllValuesFilter
from django_filters.rest_framework import DjangoFilterBackend
from requests import request
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from circuit.models import Chain, InfoChain, Product, Staff
from circuit.permissions import ListPermissions
from circuit.serializers import InfoChainSerializer, ChainCreateSerializer, ProductCreateSerializer, ProductSerializer, \
    SupplierSerializer, StaffSerializer, UpdateChainSerializer


class ChainListView(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    permission_classes = [ListPermissions]

    def get_queryset(self):
        print([x for x in InfoChain.objects.all()])
        return InfoChain.objects.all()


class InfoChainCountry(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contacts__address__country',)

    def get_queryset(self):
        return InfoChain.objects.all()


class StaticDebt(ListAPIView):
    model = InfoChain
    serializer_class = InfoChainSerializer
    filter_backends = [DjangoFilterBackend]

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
    filterset_fields = ('products__id',)

    def get_queryset(self):
        return InfoChain.objects.all()


class CreateChain(CreateAPIView):
    model = InfoChain
    serializer_class = ChainCreateSerializer


class CreateProduct(CreateAPIView):
    model = Chain.Suppler
    serializer_class = SupplierSerializer


class CreateStaff(CreateAPIView):
    model = Staff
    serializer_class = StaffSerializer


class UpdateInfoChain(UpdateAPIView):
    queryset = InfoChain.objects.filter()
    model = InfoChain
    serializer_class = UpdateChainSerializer
