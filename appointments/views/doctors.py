from django.http import HttpResponseRedirect
from django.views import generic

from appointments.models.doctor import Doctor

class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors/doctors.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
