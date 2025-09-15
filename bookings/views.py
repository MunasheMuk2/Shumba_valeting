# Renders HTML templates and handles redirects
from django.shortcuts import render, redirect

# Allows you to show success/error messages to the user
from django.contrib import messages

# Import the booking form and model
from .forms import BookingForm
from .models import Booking

# To handle manual validation errors (like double bookings)
from django.core.exceptions import ValidationError

# Restricts access to views unless the user is logged in
from django.contrib.auth.decorators import login_required


# This view handles displaying the homepage and processing the booking form
def home(request):
    error_message = None
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                # If the user is logged in, associate the booking with them
                if request.user.is_authenticated:
                    booking.user = request.user
                booking.save()
                # Show a success message and redirect to homepage
                messages.success(request, "Booking confirmed! Thank you.")
                return redirect("home")
            # If the time slot is already taken, show an error message  - feature currently not working as per Readme
            except ValidationError as e:
                messages.error(request, e.message)

    else:
        form = BookingForm()

    return render(request, "home.html", {"form": form})


# Only logged-in users can access this view
@login_required
def my_bookings(request):

    # Get all bookings made by the currently logged-in user, ordered by date & time
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
