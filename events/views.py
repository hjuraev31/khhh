from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics
from .models import Events, ImgDB
from .serializers import EventsSerializer, ImgSerializer
from django.http import request, HttpResponse
from rest_framework.response import Response
from .custom_renderers import JPEGRenderer, PNGRenderer
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

class ImageAPIView(generics.RetrieveAPIView):

    queryset = ImgDB.objects.get(id = 1)
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        renderer_classes = [JPEGRenderer]
        queryset = ImgDB.objects.get(id=self.kwargs['id']).img
        data = queryset
        return Response(data, content_type='image/jpg')

def studimg(request, name):
	idname = ImgDB.objects.filter(name=name)
	ids = [idname[x].id for x in range(len(idname))]
	return HttpResponse(str(ids))

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
