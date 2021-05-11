from django.db import models

from appointments.models.doctor import Doctor
from appointments.models.patient import Patient

class Appointment(models.Model):
    patient          = models.ForeignKey(Patient,         on_delete = models.DO_NOTHING)
    doctor           = models.ForeignKey(Doctor,          on_delete = models.DO_NOTHING)
    appointment_type = models.CharField(max_length = 200)
    start_time       = models.DateTimeField()
    end_time         = models.DateTimeField()
    details          = models.CharField(max_length = 200)

    class Meta:
        db_table = 'appointment'
