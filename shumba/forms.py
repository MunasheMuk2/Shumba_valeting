from django import forms
from .models import Booking


# Auto generate form field based on booking model
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "car_type", "package", "date", "time"]
