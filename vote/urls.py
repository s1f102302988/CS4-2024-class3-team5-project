from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('kinokotakenoko/', views.kinokotakenoko, name='kinokotakenoko'),
    path('loveormoney/', views.loveormoney, name='loveormoney'),
    path('torokko/', views.torokko, name='torokko'),
    path('room/', views.room, name='room'),
    path('vote/kinokotakenoko/', views.vote_kinokotakenoko, name='vote_kinokotakenoko'),
    path('vote/loveormoney/', views.vote_loveormoney, name='vote_loveormoney'),
    path('vote/torokko/', views.vote_torokko, name='vote_torokko'),

    ]