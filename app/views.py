from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from django.shortcuts import render
from .models import *
from .serializers import PizzaSerializers


class FilteredPizzaList(generics.ListAPIView):
  queryset = Pizza.objects.all()
  serializer_class = PizzaSerializers
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['type', 'size']


@api_view(['get'])
def pizza_list(request):
  pizzas = Pizza.objects.all()
  serializers = PizzaSerializers(pizzas, many=True)
  return Response(serializers.data)


@api_view(['post'])
def create_item(request):
  serializers = PizzaSerializers(data=request.data)
  if serializers.is_valid():
    serializers.save()
  return Response(serializers.data)


@api_view(['post'])
def update_item(request, pk):
  pizzas = Pizza.objects.get(id=pk)
  serializers = PizzaSerializers(data=request.data, instance=pizzas)
  if serializers.is_valid():
    serializers.save()
  return Response(serializers.data)


@api_view(['delete'])
def delete_item(request, pk):
  pizzas = Pizza.objects.get(id=pk)
  message = 'Pizza item has been deleted successfully!'
  pizzas.delete()
  return Response(message)