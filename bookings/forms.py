import datetime
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
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < datetime.date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_slot = cleaned_data.get("time_slot")

        if date == datetime.date.today() and time_slot:
            now = datetime.datetime.now().time()
            slot_time = datetime.datetime.strptime(time_slot, "%H:%M").time()
            if slot_time < now:
                raise forms.ValidationError(
                    "You cannot book a time slot that has already passed today."
                )

        return cleaned_data


class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "car_make_model",
            "car_reg",
            "package",
            "date",
            "time_slot",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < datetime.date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_slot = cleaned_data.get("time_slot")

        if date == datetime.date.today() and time_slot:
            now = datetime.datetime.now().time()
            slot_time = datetime.datetime.strptime(time_slot, "%H:%M").time()
            if slot_time < now:
                raise forms.ValidationError(
                    "You cannot book a time slot that has already passed today."
                )
        return cleaned_data
