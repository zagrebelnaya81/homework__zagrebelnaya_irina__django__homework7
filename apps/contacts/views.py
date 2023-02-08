from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contacts.models import Contacts


class ContactsListView(ListView):
    model = Contacts


class ContactsCreateView(CreateView):
    model = Contacts
    fields = (
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:list")


class ContactsUpdateView(UpdateView):
    model = Contacts
    fields = (
        "id",
        "name",
        "phone",
    )
    success_url = reverse_lazy("contacts:list")


class ContactsDeleteView(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts:list")
