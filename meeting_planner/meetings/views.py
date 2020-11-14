from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import NewMeetingForm


def meeting_details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting_details.html", {"meeting": meeting})


def meeting_room_details(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/meeting_room_details.html", {"room": room})


def new_meeting(request):
    if request.method == "POST":
        new_meeting_form = NewMeetingForm(request.POST)
        if new_meeting_form.is_valid():
            new_meeting_form.save()
            return redirect("home")
    else:
        new_meeting_form = NewMeetingForm()
    return render(request, "meetings/new_meeting.html", {"form": new_meeting_form})
