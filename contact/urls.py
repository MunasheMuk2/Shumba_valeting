from django.urls import path
from . import views


# Place URL routes and then connect them to our views

urlpatterns = [
    path("contact/", views.contact_view, name="contact"),
]
