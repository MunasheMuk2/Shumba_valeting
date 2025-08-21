from django.contrib import admin
from .models import Booking, Package

# Register your models here. - Allows us to register database models so we can view on admin panel
# Make sure Packages are registered
admin.site.register(Package)
admin.site.register(Booking)
