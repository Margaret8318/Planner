from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

def welcome(request):
    return render(request, "landing/welcome.html",
                  {"num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about(request):
    return HttpResponse("Author: Margaret8318")