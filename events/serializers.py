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
<<<<<<< HEAD
=======
		
>>>>>>> 159ad2393c5a950686e8f063514ca8d97dbebe42
