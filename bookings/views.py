from django.shortcuts import render, redirect
from .forms import BookingForm

# create different routes to access on our websites


def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # save booking into PostgreSQL
            return redirect("home")  # reload after success
    else:
        form = BookingForm()
    return render(request, "home.html", {"form": form})
