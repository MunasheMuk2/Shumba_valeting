# Import Django’s built-in forms system
from django import forms

# Import the Booking model, Package model, and TIME_SLOTS list from models.py
from .models import Booking, Package, TIME_SLOTS

# This form is used to create or update a Booking object in the database
# assisted by https://www.geeksforgeeks.org/python/how-to-create-a-form-using-django-forms/ & stack overflow


class BookingForm(forms.ModelForm):

    # Package dropdown field — lets the user choose a valet package
    package = forms.ModelChoiceField(
        queryset=Package.objects.all(),
        empty_label="Select a Package",
        label="Valet Package",
    )
    # Time slot dropdown field — uses TIME_SLOTS from models.py
    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        label="Preferred Time Slot",
    )

    # To connect the form to the Booking model and customizes how it looks
    class Meta:
        model = Booking

        # Fields will be included in the form
        fields = [
            "name",
            "email",
            "car_make_model",
            "car_reg",
            "package",
            "date",
            "time_slot",
        ]

        # Customize labels for specific fields (what the user sees)
        labels = {
            "car_make_model": "Car Make & Model (e.g. Toyota Hilux)",
            "car_reg": "Car Registration (optional)",
        }

        # Customize the "date" field to show a date picker
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
