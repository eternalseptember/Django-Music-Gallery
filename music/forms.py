from django import forms
from django.contrib.auth.models import User
from .models import Album, Song


class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['artist', 'title', 'genre', 'logo']


class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['title', 'file']


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

