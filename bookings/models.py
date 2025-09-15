#Assisted with models by watching tech with Tim on youtube - particulary learn Django in 20mins video
# Import Django's model system
from django.db import models

# Import built-in User model for associating bookings with logged-in users
from django.contrib.auth.models import User

# Import error class to handle validation problems
from django.core.exceptions import ValidationError


# PACKAGE MODEL
# This model represents the valeting service packages (e.g., Basic, Premium)
class Package(models.Model):
    # Name of the package (e.g., Basic Valet)
    name = models.CharField(max_length=50)
    # Price of the package (up to 9999.99 with 2 decimal places)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # package display (e.g., "Basic Valet - £25.00")
    def __str__(self):
        return f"{self.name} - £{self.price:.2f}"


# TIME SLOT OPTIONS
# A list of available time slots for booking a valet
TIME_SLOTS = [
    ("08:00", "08:00 AM"),
    ("10:00", "10:00 AM"),
    ("12:00", "12:00 PM"),
    ("14:00", "02:00 PM"),
    ("16:00", "04:00 PM"),
]

# BOOKING MODEL
# This model stores customer booking details


class Booking(models.Model):
    # Connects booking to a user account (optional, can be blank)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Make and model of the car
    car_make_model = models.CharField(max_length=150)
    car_reg = models.CharField(max_length=20, null=True, blank=True)
    # Chosen package (linked to the Package model)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=TIME_SLOTS)
    # Timestamp when the booking was created (auto-filled)
    created_at = models.DateTimeField(auto_now_add=True)
    # Whether the booking was cancelled (default is False)
    cancelled = models.BooleanField(default=False)

    class Meta:
        # Ensures the same time slot can't be booked twice on the same date
        unique_together = ("date", "time_slot")
        # Orders bookings by date and then time slot
        ordering = ["date", "time_slot"]

    def clean(self):
        # Check if another booking already exists for the same date & time slot
        if (
            Booking.objects.filter(date=self.date, time_slot=self.time_slot)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                "Sorry, this time slot is already booked. Please select another one."
            )

    # How the booking will be displayed (for admin or Django shell)
    def __str__(self):
        return (
            f"{self.name} - {self.package.name} (£{self.package.price}) "
            f"on {self.date} at {self.get_time_slot_display()}"
        )
