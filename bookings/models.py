from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Assisted by youtube channel tech with Tim


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    car_type = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.package} on {self.date}"  # auto_now_add added to automatically populate this info
