from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    context = {'form': form}
    return render(request, 'base/room_form.html', context)
    
