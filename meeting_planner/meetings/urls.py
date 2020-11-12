from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms/<int:id>', views.meeting_room_detail, name='room'),
]