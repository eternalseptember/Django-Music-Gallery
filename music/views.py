from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import operator

from .models import Album, Song
from .forms import RegisterForm, LoginForm


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class SongListView(generic.ListView):
	template_name = 'music/songs.html'
	context_object_name = 'all_songs'

	def get_queryset(self):
		return Song.objects.all()


class SearchView(generic.ListView):
	template_name = 'music/search.html'
	context_object_name = 'results'

	def get_queryset(self):
		query = self.request.GET.get('q')

		if query:	
			search_results = Song.objects.filter(
				Q(album__artist__icontains = query) | 
				Q(album__title__icontains = query) |
				Q(album__year__icontains = query) |
				Q(title__icontains = query)
			)
		return search_results


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
	fields = ['artist', 'title', 'year', 'logo']


class AlbumUpdate(UpdateView):
	model = Album
	template_name = 'music/detail_form.html'
	fields = ['artist', 'title', 'year', 'logo', 'is_favorite']

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


def Logout(request):
	logout(request)
	return redirect('music:index')


class UserLogin(FormView):
	form_class = LoginForm
	template_name = 'music/user_form.html'

	def get_context_data(self, **kwargs):
		context = super(UserLogin, self).get_context_data(**kwargs)
		context['header_text'] = 'Log In'
		context['login'] = True
		return context

	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('music:index')
			else:
				return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Inactive User', 'header_text': 'Log In', 'login': True})
		else: 
			return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Invalid Credentials', 'header_text': 'Log In', 'login': True})


class UserRegister(FormView):
	form_class = RegisterForm
	template_name = 'music/user_form.html'

	def get_context_data(self, **kwargs):
		context = super(UserRegister, self).get_context_data(**kwargs)
		context['header_text'] = 'Register New Account'
		context['register_user'] = True
		return context

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

		return render(request, self.template_name, {'form': form, 'header_text': 'Register New Account', 'register_user': True})

