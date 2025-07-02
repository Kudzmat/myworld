from django.db import models

# Create your models here.
class VibeCheckEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Vibe Check Entries'
        verbose_name = 'Vibe Check Entry'

    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=100, blank=True, null=True)
    song_selection = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.added_by} added - {self.song_selection}.'