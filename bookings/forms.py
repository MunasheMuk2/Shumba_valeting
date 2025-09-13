from django import forms
from .models import Booking, Package, TIME_SLOTS


class BookingForm(forms.ModelForm):
    package = forms.ModelChoiceField(
        queryset=Package.objects.all(),
        empty_label="Select a Package",
        label="Valet Package",
    )

    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        label="Preferred Time Slot",
    )

    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "car_make_model",
            "car_reg",
            "package",
            "date",
            "time_slot",
        ]
        labels = {
            "car_make_model": "Car Make & Model (e.g. Toyota Hilux)",
            "car_reg": "Car Registration (optional)",
        }
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
