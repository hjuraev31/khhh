from django.db import models

class Events(models.Model):
	event = models.CharField(max_length=255)
	game = models.CharField(max_length=255)
	place = models.CharField(max_length=128)
	date = models.DateField(auto_now=False)
	time = models.TimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.event
# Create your models here.
