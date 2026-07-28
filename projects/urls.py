from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
	path('personal-projects/', views.PersonalProjectoView.as_view(), name="personal_projects"),
    path('personal-projects/<slug:slug>', views.PersonalProjectDetailView.as_view(), name="personal_project_detail"),
	path('short-stories/', views.ShortStoryView.as_view(), name="short_stories"),
	path('short-stories/<slug:slug>', views.ShortStoryDetailView.as_view(), name="short_story_detail"),
	]