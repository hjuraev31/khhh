from django.shortcuts import render
from rest_framework import generics
from .models import Events
from .serializers import EventsSerializer
from django.http import request, HttpResponse
class EventList(generics.ListCreateAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

class DetailEvent(generics.RetrieveUpdateDestroyAPIView):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer

def bodyText(request, pk):
	events = Events.objects.filter(pk=pk)
	text = Events.objects.get(pk=pk)

	return HttpResponse(text) #render(request, 'textShow/text.html/', {'text': text, events:events})

def byName(request, name):
	groupStudent = ["Samandarbek","Saydiabzal","Abrorbek","Begimqulov","Xusniddin","Faxriddin","Xikmatov","Seitov","Dostonbek","Madinabonu","Anvarjonov","Jaxongir","Berdiyorov","Sayidov","Ibrohimov"]
	if name in groupStudent:
		idname = Events.objects.filter(student_id=name)
		names = []
		for i in range(len(idname)):
			names.append(idname[i].id)
		print(names)
		names.sort()
	return HttpResponse(str(names))
