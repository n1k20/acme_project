from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 1


class BirthdayMixin:
    model = Birthday


class BirthdayCreateView(BirthdayMixin, CreateView):
    form_class = BirthdayForm


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    form_class = BirthdayForm


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthdays'] = calculate_birthday_countdown(self.object.birthday)
        return context
