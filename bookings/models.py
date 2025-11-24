from django.db import models
from django.contrib.auth.models import User

# Database models
# Assisted by youtube channel tech with Tim


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.name} - £{self.price}"


TIME_SLOTS = [
    ("09-11", "9am - 11am"),
    ("11-13", "11am - 1pm"),
    ("13-15", "1pm - 3pm"),
    ("15-17", "3pm - 5pm"),
]


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    car_make_model = models.CharField(
        max_length=150,
    )
    car_reg = models.CharField(max_length=20, null=True, blank=True)  # new field
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
    created_at = models.DateTimeField(auto_now_add=True)

    cancelled = models.BooleanField(default=False)

    class Meta:
        unique_together = ("date", "time_slot")  # Prevents double booking of a slot

    def __str__(self):
        return (
            f"{self.name} - {self.package.name} (£{self.package.price}) "
            f"on {self.date} at {self.get_time_slot_display()}"
        )
