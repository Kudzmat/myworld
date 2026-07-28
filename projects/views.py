from django.shortcuts import render
from django.contrib import messages
from .models import PersonalProject, ShortStory
from django.views import generic



class PersonalProjectoView(generic.ListView):
    model = PersonalProject
    template_name = "projects/projects.html"
    paginate_by = 10

class PersonalProjectDetailView(generic.DetailView):
    model = PersonalProject
    template_name = "projects/project_detail.html"


class ShortStoryView(generic.ListView):
    model = ShortStory
    template_name = "projects/short_stories.html"
    paginate_by = 10


class ShortStoryDetailView(generic.DetailView):
    model = ShortStory
    template_name = "projects/short_story_detail.html"
