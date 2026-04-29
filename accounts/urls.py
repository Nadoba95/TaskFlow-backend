from django.urls import path
from .views import register, MeView

urlpatterns = [
    path("register/", register),
    path("me/", MeView.as_view()),
]
