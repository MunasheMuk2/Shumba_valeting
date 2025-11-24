from django.urls import path
from . import views

# Place URL routes and then connect them to our views

urlpatterns = [
    path("", views.home, name="home"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
]
