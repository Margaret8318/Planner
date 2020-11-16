from django.urls import path, include
from . import views

urlpatterns = [
    # path('usersdashboard/', views.users_dashboard, name="user_dashboard"),
    path('accounts/', include("django.contrib.auth.urls")),
]