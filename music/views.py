from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from .models import Album, Song
from .forms import UserForm


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	# The default context object name is 'object_list'.
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class SongListView(generic.ListView):
	template_name = 'music/songs.html'
	context_object_name = 'all_songs'

	def get_queryset(self):
		return Song.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['link_detail'] = True
		context['header_text'] = "All Songs"
		return context


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'title', 'genre', 'logo']


class AlbumUpdate(UpdateView):
	model = Album
	template_name = 'music/detail_form.html'
	fields = ['artist', 'title', 'genre', 'logo', 'is_favorite']

	def get_context_data(self, **kwargs):
		context = super(AlbumUpdate, self).get_context_data(**kwargs)
		context['link_album_update'] = True
		context['header_text'] = "Edit Album Details"
		return context


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


def AlbumFavorite(request, **kwargs):
	album = get_object_or_404(Album, pk = kwargs['pk'])

	try:
		album.is_favorite = not album.is_favorite
		album.save()
	except (KeyError, Album.DoesNotExist):
		return HttpResponse("Album not found.")
	else:
		return redirect('music:index')


class SongCreate(CreateView):
	model = Song
	template_name = 'music/detail_form.html'
	fields = ['title', 'file', 'track_number', 'is_favorite']

	def get_context_data(self, **kwargs):
		album_number = self.kwargs['pk']
		context = super(SongCreate, self).get_context_data(**kwargs)
		context['album'] = Album.objects.get(id = album_number)
		context['link_song_create'] = True
		context['header_text'] = "Add New Song"
		return context

	def form_valid(self, form):
		album_number = self.kwargs['pk']
		form.instance.album = Album.objects.get(id = album_number)
		return super(SongCreate, self).form_valid(form)


class SongUpdate(UpdateView):
	model = Song
	pk_url_kwarg = 'song_id'
	template_name = 'music/detail_form.html'
	fields = ['title', 'file', 'track_number', 'is_favorite']

	def get_context_data(self, **kwargs):
		album_number = self.kwargs['pk']
		context = super(SongUpdate, self).get_context_data(**kwargs)
		context['album'] = Album.objects.get(id = album_number)
		context['link_song_update'] = True
		context['header_text'] = "Edit Song Details"
		return context


class SongDelete(DeleteView):
	model = Song
	pk_url_kwarg = 'song_id'

	def get_success_url(self):
		return reverse_lazy('music:detail', kwargs = { 'pk': self.kwargs['pk'] })


def SongFavorite(request, **kwargs):
	song = get_object_or_404(Song, pk = kwargs['song_id'])

	try:
		song.is_favorite = not song.is_favorite
		song.save()
	except (KeyError, Song.DoesNotExist):
		return HttpResponse("Song not found.")
	else:
		return redirect('music:detail', pk = kwargs['pk'] )


class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form}) 

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			# cleaned (normalized data)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form': form})

