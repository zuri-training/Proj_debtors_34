from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import post

class postCreateView(CreateView):
    model = post
    fields = [
        "Name"
        "Student_ID"
        "Email"
        "Debt"
        "Amount_paid"
        "Status"
    ]
    template_name = 'home.html'
    success_url = 'list.html'


class postListView(ListView):
    model = post
    template_name = 'list.html'


class postDetailView(DetailView):
    model = post
    template_name = 'detail.html'

class postUpdateView(UpdateView):
    model = post
    fields = [
        "Name"
        "Student_ID"
        "Email"
        "Debt"
        "Amount_paid"
        "Status"
    ]
    template_name = 'update.html'
    success_url = '/'

class postDeleteView(DeleteView):
    model = post
    template_name =  'delete.html'
    success_url = '/'

