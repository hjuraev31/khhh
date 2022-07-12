from rest_framework import serializers
from .models import Events, ImgDB

class EventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Events
		fields = '__all__'
		

class ImgSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImgDB
		fields = '__all__'
