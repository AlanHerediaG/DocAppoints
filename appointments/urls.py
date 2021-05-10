from django.urls import path

from appointments.views.index import index
from appointments.views import appointments
from appointments.views import doctors
from appointments.views import patients

urlpatterns = [
    path('', index, name='index'),
    path('citas/', appointments.AppointmentListView.as_view(), name='appointments'),
    path('citas/agendar_cita/', appointments.AppointmentCreateView.as_view(), name='agendar_cita'),

    path('doctores/', doctors.DoctorListView.as_view(), name='doctors'),
    path('doctores/registrar_doctor/', doctors.DoctorCreateView.as_view(), name='registrar_doctor'),
    
    path('pacientes/', patients.PatientListView.as_view(), name='patients'),
    path('pacientes/registrar_paciente/', patients.PatientCreateView.as_view(), name='registrar_paciente'),
]