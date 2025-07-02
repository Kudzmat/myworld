from django.contrib import admin
from .models import VibeCheckEntry


@admin.register(VibeCheckEntry)
class VibeCheckEntryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'song_selection', 'added_by')
    search_fields = ('song_selection', 'added_by')
    ordering = ('-timestamp',)
    list_per_page = 20