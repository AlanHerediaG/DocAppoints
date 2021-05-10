from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from appointments.models.doctor import Doctor

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctors.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DoctorCreateView(CreateView):
    model = Doctor
    fields = ('name', 'first_last_name', 'second_last_name', 'birthday', 'speciality')
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctors')