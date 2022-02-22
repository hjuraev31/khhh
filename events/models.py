from django.db import models

class Events(models.Model):
	student_id = models.TextField(default='')
	text = models.TextField(default='')
	def __str__(self):
		return self.text[:5]
# Create your models here.
