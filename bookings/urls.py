from django.urls import path
from . import views

# Place URL routes and then connect them to our views

urlpatterns = [
    path("", views.home, name="home"),
]
