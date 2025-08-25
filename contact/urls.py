from django.urls import path
from .views import contact_view


# Place URL routes and then connect them to our views

urlpatterns = [
    path("", contact_view, name="contact"),
]
