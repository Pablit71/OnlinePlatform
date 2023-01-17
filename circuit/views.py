from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView

from circuit.models import BaseModel
from circuit.serializers import BaseModelSerializer


# Create your views here.
class BaseModelView(ListAPIView):
    model = BaseModel
    serializer_class = BaseModelSerializer

    def get_queryset(self):
        return BaseModel.objects.all()
