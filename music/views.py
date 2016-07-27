from django.views import generic
from .models import Album


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	# The default context object name is 'object_list'.
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'