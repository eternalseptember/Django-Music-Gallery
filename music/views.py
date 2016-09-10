from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	# The default context object name is 'object_list'.
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'title', 'genre', 'logo']


class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'title', 'genre', 'logo']


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


class SongCreate(CreateView):
	model = Song
	template_name = 'music/song_form.html'
	# fields = ['album', 'title', 'file', 'track_number', 'is_favorite']
	fields = ['title', 'file', 'track_number', 'is_favorite']

	def form_valid(self, form):
		album_number = self.kwargs['pk']
		form.instance.album = Album.objects.get(id = album_number)
		return super(SongCreate, self).form_valid(form)


class SongDelete(DeleteView):
	model = Song
	# Try to figure out how to direct back to the album's page
	success_url = reverse_lazy('music:detail')


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

