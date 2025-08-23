from django.db import models
from django.contrib.auth.models import User

# Database models
# Assisted by youtube channel tech with Tim


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - £{self.price}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    car_type = models.CharField(max_length=100)
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE
    )  # now linked to package model
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add added to automatically populate this info

    def __str__(self):
        return (
            f"{self.name} - {self.package.name} (£{self.package.price}) on {self.date}"
        )
