from django.shortcuts import render
from django.contrib import messages
from .models import PersonalProject
from django.views import generic



class PersonalProjectoView(generic.ListView):
    model = PersonalProject
    template_name = "projects/projects.html"
    paginate_by = 10

class PersonalProjectDetailView(generic.DetailView):
    model = PersonalProject
    template_name = "projects/project_detail.html"
