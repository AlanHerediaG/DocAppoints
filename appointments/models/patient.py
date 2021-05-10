from django.db import models

class Patient(models.Model):
    name             = models.CharField(max_length = 30)
    first_last_name  = models.CharField(max_length = 30)
    second_last_name = models.CharField(max_length = 30)
    birthday         = models.DateTimeField()
    sex              = models.CharField(max_length = 20)
    registry_date    = models.DateField()
    details          = models.CharField(max_length = 200)

    class Meta:
        db_table = 'patient'

    def __str__(self):
        return f"{self.name} {self.first_last_name} {self.second_last_name}"