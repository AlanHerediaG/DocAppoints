from django.db import models

from appointments.models.doctor import Doctor
from appointments.models.patient import Patient
#
class AppointmentType(models.Model):
    description = models.CharField(max_length = 200)

    class Meta:
        db_table = 'appointment_type'

class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()

    class Meta:
        db_table = 'time_slot'

class Appointment(models.Model):
    patient          = models.ForeignKey(Patient,         on_delete = models.DO_NOTHING)
    doctor           = models.ForeignKey(Doctor,          on_delete = models.DO_NOTHING)
    appointment_type = models.ForeignKey(AppointmentType, on_delete = models.DO_NOTHING)
    time_slot        = models.ForeignKey(TimeSlot,        on_delete = models.DO_NOTHING)
    details          = models.CharField(max_length = 200)

    class Meta:
        db_table = 'appointment'
