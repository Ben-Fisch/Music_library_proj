from django.http import request
from django.urls import path
from . import views


urlpatterns = [
    path('songs/', views.SongList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
    path('songs/<int:pk>/likes/', views.SongLikes.as_view())

]