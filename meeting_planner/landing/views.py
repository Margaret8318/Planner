from datetime import datetime

from django.core.paginator import PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# from django.views.generic import ListView, DetailView, TemplateView
from meetings.models import Meeting, Room

class WelcomeView(View):
    def get(self, request):
        all_meetings = Meeting.objects.all()
        paginated_meetings =  Paginator(all_meetings, 2)
        pages = request.GET.get('page', 1)
        try:
            meetings = paginated_meetings.page(pages)
        except PageNotAnInteger:
            meetings = paginated_meetings.page(1)
        return render(request, "landing/welcome.html",
                    {"meetings": meetings,
                    "rooms": Room.objects.all()})
    # template_name = 'landing/welcome.html'
    # def get_context_data(self, **kwargs):
    #     context= {'meetings': Meeting.objects.all(), "rooms": Room.objects.all()}
    #     return context



def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")


def about(request):
    return HttpResponse("Author: Margaret8318")
