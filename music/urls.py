from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/register
	url(r'^register/$', views.UserRegister.as_view(), name='register'),
	# /music/login
	url(r'^login/$', views.UserLogin.as_view(), name="login"),
	# /music/logout
	url(r'^logout/$', views.Logout, name="logout"),


	# /music/album/add
	url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
	# /music/album/<album_id>/update/
	url(r'album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),
	# /music/album/<album_id>/favorite
	url(r'album/(?P<pk>[0-9]+)/favorite/$', views.AlbumFavorite, name="album-favorite"),
	# /music/album/<album_id>/delete/
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
	# /music/album/<album_id>/add/
	url(r'album/(?P<pk>[0-9]+)/add/$', views.SongCreate.as_view(), name="song-add"),
	# /music/album/<album_id>/<song_id>/update
	url(r'album/(?P<pk>[0-9]+)/(?P<song_id>[0-9]+)/update/$', views.SongUpdate.as_view(), name="song-update"),
	# /music/album/<album_id>/<song_id>/favorite
	url(r'album/(?P<pk>[0-9]+)/(?P<song_id>[0-9]+)/favorite/$', views.SongFavorite, name="song-favorite"),
	# /music/album/<album_id>/<song_id>/delete/
	url(r'album/(?P<pk>[0-9]+)/(?P<song_id>[0-9]+)/delete/$', views.SongDelete.as_view(), name="song-delete"),
	# /music/album/<album_id>
	url(r'album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


	# /music/songs/
	url(r'songs/$', views.SongListView.as_view(), name='songs'),
	# /music/search
	url(r'search/$', views.SearchView.as_view(), name='search'),
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),

]
