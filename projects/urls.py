from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
	path('personal-projects/', views.PersonalProjectoView.as_view(), name="personal_projects"),
    path('personal-projects/<slug:slug>', views.PersonalProjectDetailView.as_view(), name="personal_project_detail"),
	]