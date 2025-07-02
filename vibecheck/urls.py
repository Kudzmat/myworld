from django.urls import path
from . import views


app_name = "vibe_check"

urlpatterns = [
    path('open-source-playlist', views.vibe_check, name="vibe_check"),
	]