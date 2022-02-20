from django.shortcuts import render
from rest_framework import generics
from .models import Events
from .serializers import EventsSerializer
class EventList(generics.ListAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

class DetailEvent(generics.RetrieveAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer
