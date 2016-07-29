from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.
class Album(models.Model):
	user = models.ForeignKey(User, default = 1)
	artist = models.CharField(max_length = 250)
	title = models.CharField(max_length = 500)
	genre = models.CharField(max_length = 100)
	logo = models.FileField()
	is_favorite = models.BooleanField(default = False)

	def __str__(self):
		return self.title + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	title = models.CharField(max_length = 250)
	file = models.FileField(default = '')
	is_favorite = models.BooleanField(default = False)

	def __str__(self):
		return self.title