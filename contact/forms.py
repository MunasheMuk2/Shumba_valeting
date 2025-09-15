# Import Django's forms system
from django import forms

# Import the Contact model from models.py
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
