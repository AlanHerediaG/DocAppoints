from django.http import HttpResponseRedirect
from django.views import generic

from appointments.models.appointment import Appointment

class AppointmentListView(generic.ListView):
    model = Appointment
    template_name = 'appointments/appointments.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
