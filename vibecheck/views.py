import os
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from .models import VibeCheckEntry
from .forms import SongSearchForm

# Load environment variables
load_dotenv()

# Logger setup
logger = logging.getLogger(__name__)

# Load and assert required env vars
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')
PLAYLIST_ID = os.getenv('VIBE_CHECK_PLAYLIST_ID')
SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "
CACHE_PATH = ".cache-vibecheck"

assert CLIENT_ID, "SPOTIFY_CLIENT_ID is missing from environment."
assert CLIENT_SECRET, "SPOTIFY_CLIENT_SECRET is missing from environment."
assert SPOTIFY_REDIRECT_URI, "SPOTIFY_REDIRECT_URI is missing from environment."
assert PLAYLIST_ID, "VIBE_CHECK_PLAYLIST_ID is missing from environment."

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=SCOPE,
        cache_path=CACHE_PATH
    ))

# Get names of contributors
def get_contributor_names():
    contributors = VibeCheckEntry.objects.all()
    seen = set()
    names = []

    for contributor in contributors:
        name = contributor.added_by
        if name not in seen:
            names.append(name)
            seen.add(name) # Avoid multiple entries of the same person 

    names.sort()
    return names


def vibe_check(request):
    sp = get_spotify_client()
    contributors = get_contributor_names()
    search_results = []
    added_track_name = None
    contributor_name = None
    display_name = True

    if request.method == "POST":
        form = SongSearchForm(request.POST)
        if form.is_valid():
            # Get the form details
            query = form.cleaned_data["query"] # song search query
            contributor_name = form.cleaned_data.get("contributor_name")
            

            # Store contributor details in the session
            request.session["contributor_name"] = contributor_name

            # Search for the song on Spotify
            try:
                result = sp.search(q=query, type="track", limit=3)
                search_results = result["tracks"]["items"]
            except Exception as e:
                logger.error(f"Search failed: {e}")
                messages.error(request, "Spotify search failed. Try again.")
                return redirect("vibe_check:vibe_check")
    else:
        form = SongSearchForm()

    # If user clicks "add" button for a specific track
    if "add_track" in request.GET:
        track_uri = request.GET.get("add_track")
        try:
            # Retrieve contributor details from the session
            contributor_name = request.session.get("contributor_name", "Anonymous")

            sp.playlist_add_items(PLAYLIST_ID, [track_uri])  # Add the track to the playlist
            added_track_name = sp.track(track_uri)["name"] # Get the track name

            # Save the entry to the database
            VibeCheckEntry.objects.create(
                added_by=contributor_name,
                song_selection=added_track_name,
            )
            messages.success(request, f"Thanks for contributing {contributor_name}! '{added_track_name}' was added to the Vibe Check playlist!")
            return redirect("vibe_check:vibe_check")
            
        except Exception as e:
            logger.error(f"Add to playlist failed: {e}")
            messages.error(request, "Could not add the track. Try again.")

    context = {
        "form": form,
        "results": search_results,
        "added_track_name": added_track_name,
        "playlist_id": PLAYLIST_ID,
        "contributor_names": contributors,
    }

    return render(request, "vibecheck/vibecheck.html", context=context)