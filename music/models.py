from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
class Album(models.Model):
	#user = models.ForeignKey(User, default = 1)
	artist = models.CharField(max_length = 250)
	title = models.CharField(max_length = 500)
	year = models.CharField(max_length = 4)
	logo = models.FileField()
	is_favorite = models.BooleanField(default = False)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	title = models.CharField(max_length = 250)
	file = models.FileField(default = '')
	track_number = models.IntegerField(default = 1)
	is_favorite = models.BooleanField(default = False)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk': self.album.id})

	def __str__(self):
		return self.title


@receiver(post_delete, sender = Song)
def song_post_delete(sender, **kwargs):
	song = kwargs['instance']
	storage = song.file.storage
	path = song.file.path
	storage.delete(path)


@receiver(post_delete, sender = Album)
def album_post_delete(sender, **kwargs):
	album = kwargs['instance']
	storage = album.logo.storage
	path = album.logo.path
	storage.delete(path)

