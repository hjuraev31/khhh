from django.shortcuts import render
from rest_framework import generics
from .models import Events, ImgDB
from .serializers import EventsSerializer, ImgSerializer
from django.http import request, HttpResponse
import requests as req
class EventList(generics.ListCreateAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

class DetailEvent(generics.RetrieveUpdateDestroyAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

class DeleteDataBase(generics.DestroyAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

class ImgList(generics.ListCreateAPIView):
	queryset = ImgDB.objects.all()
	serializer_class = ImgSerializer

def bodyText(request, pk):
	events = Events.objects.filter(pk=pk)
	text = Events.objects.get(pk=pk)

	return HttpResponse(text) #render(request, 'textShow/text.html/', {'text': text, events:events})

def byName(request, name):
	msg = req.get("https://qqqw.ru/?users=true")
	groupStudent = msg.json()
	if name in groupStudent:
		idname = Events.objects.filter(student_id=name)
		names = []
		for i in range(len(idname)):
			names.append(idname[i].id)
		print(names)
		names.sort()
		return HttpResponse(str(names))
	else:
		return HttpResponse("🖕")
	
def delApi(request):
	ids = Events.objects.all()
	idOut = [ids[x].id for x in range(len(ids))]
	return HttpResponse(str(idOut))
