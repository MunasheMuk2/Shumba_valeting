from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - £{self.price:.2f}"


TIME_SLOTS = [
    ("08:00", "08:00 AM"),
    ("10:00", "10:00 AM"),
    ("12:00", "12:00 PM"),
    ("14:00", "02:00 PM"),
    ("16:00", "04:00 PM"),
]


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    car_make_model = models.CharField(max_length=150)
    car_reg = models.CharField(max_length=20, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=TIME_SLOTS)
    created_at = models.DateTimeField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)

    class Meta:
        unique_together = ("date", "time_slot")
        ordering = ["date", "time_slot"]

    def clean(self):
        if (
            Booking.objects.filter(date=self.date, time_slot=self.time_slot)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                "Sorry, this time slot is already booked. Please select another one."
            )

    def __str__(self):
        return (
            f"{self.name} - {self.package.name} (£{self.package.price}) "
            f"on {self.date} at {self.get_time_slot_display()}"
        )
