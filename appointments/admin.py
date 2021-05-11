from django.contrib import admin
from appointments.models.doctor import Doctor
from appointments.models.patient import Patient
from appointments.models.appointment import Appointment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)