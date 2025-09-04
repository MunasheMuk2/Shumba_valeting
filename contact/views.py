from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves to database
            return redirect("home")  # redirect after success
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
