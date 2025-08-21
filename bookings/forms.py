from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "car_type", "package", "date", "time"]
        # Date widget from - https://www.geeksforgeeks.org/python/django-form-field-custom-widgets/
        # time field - https://studygyaan.com/django/date-picker-in-django#google_vignette
        widgets = {
            "date": forms.SelectDateWidget(),
            "time": forms.TimeInput(attrs={"type": "time"}),  # clock picker
        }
