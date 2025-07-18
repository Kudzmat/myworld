from django import forms
from .models import VibeCheckEntry

class SongSearchForm(forms.Form):
    query = forms.CharField(label="Search a Song", max_length=100)
    contributor_name = forms.CharField(
        label="Your Name/Nickname",
        max_length=100,
        required=False,
        help_text="I'll show this as your contributor name. If you leave it blank, I’ll use 'Anonymous👽.' "
    )
