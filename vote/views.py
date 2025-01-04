from django.shortcuts import render

def room(request, room_name):
    return render(request, "vote/room.html", {"room_name": room_name})
def index(request):
    return render(request, "vote/index.html")

def kinokotakenoko(request):
    return render(request, "vote/kinokotakenoko.html")

def loveormoney(request):
    return render(request, "vote/loveormoney.html")

def torokko(request):
    return render(request, "vote/torokko.html")

def room(request):
    return render(request, "vote/room.html")
