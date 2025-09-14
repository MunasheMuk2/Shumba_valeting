from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def home(request):
    error_message = None
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)  # Don't save yet
                # Assign the logged-in user if authenticated
                if request.user.is_authenticated:
                    booking.user = request.user
                booking.save()  # Now save to DB
                messages.success(request, "Booking confirmed! Thank you.")
                return redirect("home")  # Prevent resubmission
            except ValidationError as e:
                # Show validation error as JavaScript alert
                error_message = e.message
                form.add_error(None, e.message)
    else:
        form = BookingForm()

    return render(request, "home.html", {"form": form})


@login_required
def my_bookings(request):
    # Get all bookings for the logged-in user
    bookings = Booking.objects.filter(user=request.user).order_by("date", "time_slot")

    cancel_id = request.GET.get("cancel")
    if cancel_id:
        try:
            booking = Booking.objects.get(id=cancel_id, user=request.user)
            booking.delete()  # or set booking.cancelled = True if you add a cancelled field
            messages.success(request, "Booking cancelled successfully.")
            return redirect("my_bookings")
        except Booking.DoesNotExist:
            messages.error(request, "Booking not found.")

    context = {"bookings": bookings}

    return render(request, "bookings/my_bookings.html", {"bookings": bookings})
