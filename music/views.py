#from django.http import Http404 		# get_object_or_404
#from django.http import HttpResponse	# render index
#from django.template import loader		# render index
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# The commented out sections are one way of rendering a template
def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	#context = {'all_albums': all_albums}
	#return HttpResponse(template.render(context, request))
	return render(request, 'music/index.html', {'all_albums': all_albums})


# Commented out section is old way of rendering page or 404
def detail(request, album_id):
	#try:
	#	album = Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
	#	raise Http404("Album does not exist.")
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album':album,
			'error_mesasge': "You did not select a valid song.",
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})

