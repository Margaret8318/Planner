from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room


def welcome(request):
    return render(request, "landing/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "rooms": Room.objects.all()})


def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")


def about(request):
    return HttpResponse("Author: Margaret8318")
