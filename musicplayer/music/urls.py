from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),  # IndexView is a class, so use .as_view() to read it as a function

    path('register/', views.UserFormView.as_view(), name='register'),  # IndexView is a class, so use .as_view() to read it as a function

    path('logout_user/', views.LogoutView.as_view(), name='logout_user'),

    path('login_user/', views.login_user, name='login_user'),

    path('<int:album_id>/create_song/', views.create_song, name='create_song'),

    path('songs/<str:filter_by>/', views.songs, name='songs'),

    path('<int:album_id>/delete_song/<int:song_id>', views.delete_song, name='delete_song'),

    # /music/71/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.create_album, name='album-add'),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/71/favorite/
    path('<int:album_id>/favorite_album/', views.favorite_album, name='favorite_album'),

    path('<int:song_id>/favorite_song/<int:album_id>/', views.favorite_song, name='favorite_song'),
]
