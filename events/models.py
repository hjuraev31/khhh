from django.db import models

class Events(models.Model):
	student_id = models.TextField(default='')
	text = models.TextField(default='')
	def __str__(self):
		return str(self.student_id)
# Create your models here.
