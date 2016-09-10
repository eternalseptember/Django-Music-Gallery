from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /music/album/add
	url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
	# /music/album/<album_id>
	url(r'album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# /music/album/<album_id>/update/
	url(r'album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),
	# /music/album/<album_id>/delete/
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
	# /music/register
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	# /music/album/<album_id>/add/
	url(r'album/(?P<pk>[0-9]+)/add/$', views.SongCreate.as_view(), name="song-add"),
	# /music/album/<album_id>/<song_id>/delete/
	url(r'album/(?P<pk>[0-9]+)/(?P<song_id>[0-9]+)/delete/$', views.SongDelete.as_view(), name="song-delete")

	# /music/album/<album_id>/favorite
	#url(r'album/(?P<pk>[0-9]+)/favorite/$', views.AlbumFavorite.as_view(), name="album-favorite")
]
