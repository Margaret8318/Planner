from django.urls import path
from . import views

urlpatterns = [
    path('meetings/<int:id>', views.meeting_details, name='meeting'),
    path('rooms/<int:id>', views.meeting_room_details, name='room'),
    path('meetings/new_meeting', views.new_meeting, name='new_meeting'),
]
