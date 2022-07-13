from rest_framework import serializers
from .models import Events, ImgDB,TgDB

class EventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Events
		fields = '__all__'
		

class ImgSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImgDB
		fields = '__all__'

class TgUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = TgDB
		fields = '__all__'
