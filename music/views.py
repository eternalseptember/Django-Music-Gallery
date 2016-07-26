# The commented out sections are one way of rendering a template

from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album


def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	#context = {'all_albums': all_albums}
	#return HttpResponse(template.render(context, request))
	return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist.")
	return render(request, 'music/detail.html', {'album': album})