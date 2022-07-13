from statistics import mode
from django.db import models

class Events(models.Model):
	student_id = models.TextField(default='')
	text = models.TextField(default='')
	def __str__(self):
		return str(self.text)

class ImgDB(models.Model):
	name = models.TextField(default='')
	img = models.ImageField(upload_to ='uploads/%Y/%m/%d/')

	def __str__(self):
		return self.name

class TgDB(models.Model):
	name = models.TextField(default='')
	chat_id = models.TextField(default='')
	status = models.BooleanField(default=False)

	def __str__(self) -> str:
		return str(self.name)