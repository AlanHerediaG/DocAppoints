from django.urls import path

from appointments.views.index import index
from appointments.views.doctors import DoctorListView
from appointments.views.appointments import AppointmentListView
from appointments.views.patients import PatientListView

urlpatterns = [
    path('', index, name='index'),
    path('citas/', AppointmentListView.as_view(), name='appointments'),
    path('doctores/', DoctorListView.as_view(), name='doctors'),
    path('pacientes/', PatientListView.as_view(), name='patients'),
]