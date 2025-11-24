from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
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
            "car_make_model": "Car Make & Model e.g. Toyota Hilux",
        }
        # Date widget from - https://www.geeksforgeeks.org/python/django-form-field-custom-widgets/
        # time field - https://studygyaan.com/django/date-picker-in-django#google_vignette
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
