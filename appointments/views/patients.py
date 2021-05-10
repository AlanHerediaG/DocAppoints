from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from appointments.models.patient import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patients.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PatientCreateView(CreateView):
    model = Patient
    fields = ('name', 'first_last_name', 'second_last_name', 'birthday', 'sex', 'registry_date', 'details')
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patients')