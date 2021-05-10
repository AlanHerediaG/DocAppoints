from django.http import HttpResponseRedirect
from django.views import generic

from appointments.models.patient import Patient

class PatientListView(generic.ListView):
    model = Patient
    template_name = 'patients/patients.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
