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
        date = self.cleaned_data.get("date")
        if date and date < datetime.date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_slot = cleaned_data.get("time_slot")

        if date == datetime.date.today() and time_slot:
            now = datetime.datetime.now().time()

            # Extract first hour from slot like "15-17"
            try:
                start_hour = int(time_slot.split("-")[0])
                slot_time = datetime.time(start_hour, 0)
            except Exception:
                raise forms.ValidationError("Invalid time slot format.")

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
        date = self.cleaned_data.get("date")
        if date and date < datetime.date.today():
            raise forms.ValidationError("You cannot book a date in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_slot = cleaned_data.get("time_slot")

        if date == datetime.date.today() and time_slot:
            now = datetime.datetime.now().time()

            # Extract the starting hour exactly the same way
            try:
                start_hour = int(time_slot.split("-")[0])
                slot_time = datetime.time(start_hour, 0)
            except Exception:
                raise forms.ValidationError("Invalid time slot format.")

            if slot_time < now:
                raise forms.ValidationError(
                    "You cannot book a time slot that has already passed today."
                )

        return cleaned_data
