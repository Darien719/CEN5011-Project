from pages.models import Event
from django.views import View
from .forms import CreateMeetingForm
from django.shortcuts import render

class CreateMeetingView(View):

    return_address = '/'

    def get(self, request, *args, **kwargs):
        form = CreateMeetingForm()
        return render(request, 'form.html', {'form': form, 'title': 'Create Meeting', 'return_address': self.return_address})

    def post(self, request, *args, **kwargs):
        form = CreateMeetingForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            event = Event(host_id = request.user.id, **form.cleaned_data)
            event.save()
        else:
            pass
