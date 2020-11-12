from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def meeting_room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/meeting_room_detail.html", {"room": room})