from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import BookingForm
from .models import Booking


def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                if request.user.is_authenticated:
                    booking.user = request.user
                booking.save()
                messages.success(request, "Booking confirmed! Thank you.")
                return redirect("home")  # Prevent resubmission
            except IntegrityError:
                messages.error(
                    request,
                    "Sorry, this time slot is already booked. Please select another time.",
                )
                return render(request, "home.html", {"form": form})
    else:
        form = BookingForm()

    return render(request, "home.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("date", "time_slot")

    cancel_id = request.GET.get("cancel")
    if cancel_id:
        try:
            booking = Booking.objects.get(id=cancel_id, user=request.user)
            booking.delete()
            messages.success(request, "Booking cancelled successfully.")
            return redirect("my_bookings")
        except Booking.DoesNotExist:
            messages.error(request, "Booking not found.")

    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        form = BookingUpdateForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Booking updated successfully.")
                return redirect("my_bookings")
            except IntegrityError:
                messages.error(
                    request, "That time slot is already taken. Please choose another."
                )
    else:
        form = BookingUpdateForm(instance=booking)

    return render(request, "bookings/edit_booking.html", {"form": form})
