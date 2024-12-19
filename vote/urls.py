from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('kinokotakenoko/', views.kinokotakenoko, name='kinokotakenoko'),
    path('loveormoney/', views.loveormoney, name='loveormoney'),
    path('torokko/', views.torokko, name='torokko')
]