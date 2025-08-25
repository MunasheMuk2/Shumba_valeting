from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.db import IntegrityError


def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Saves to PostgreSQL
                messages.success(request, "Booking confirmed! Thank you.")
                return redirect("home")  # Prevent resubmission
            except IntegrityError:
                messages.error(
                    request,
                    "Sorry, this time slot is already booked. Please select another time.",
                )
    else:
        form = BookingForm()

    return render(request, "home.html", {"form": form})
