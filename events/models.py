from django.db import models

class Events(models.Model):
	event = models.CharField(max_length=255)
	game = models.CharField(max_length=255)
	place = models.CharField(max_length=128)
	date = models.DateField()
	time = models.TimeField()

	def __str__(self):
		return self.event
# Create your models here.
