import os
import json
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SPOTIFY_REFRESH_TOKEN = os.getenv('SPOTIPY_REFRESH_TOKEN')
SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "
CACHE_PATH = ".cache-vibecheck"

assert CLIENT_ID, "SPOTIPY_CLIENT_ID is missing from environment."
assert CLIENT_SECRET, "SPOTIPY_CLIENT_SECRET is missing from environment."
assert SPOTIFY_REDIRECT_URI, "SPOTIPY_REDIRECT_URI is missing from environment."


def _seed_cache_from_env():
    """Bootstrap the on-disk token cache from SPOTIPY_REFRESH_TOKEN when no cache
    file exists yet (e.g. a fresh Heroku dyno, or a fresh local checkout). Spotipy
    treats the seeded token as expired and refreshes it immediately, then keeps
    the resulting (possibly rotated) refresh token on disk for the rest of the
    process's life."""
    if os.path.exists(CACHE_PATH) or not SPOTIFY_REFRESH_TOKEN:
        return

    seed_token_info = {
        "access_token": "",
        "token_type": "Bearer",
        "expires_in": 0,
        "scope": SCOPE.strip(),
        "expires_at": 0,
        "refresh_token": SPOTIFY_REFRESH_TOKEN,
    }
    with open(CACHE_PATH, "w") as f:
        json.dump(seed_token_info, f)


def get_spotify_client():
    _seed_cache_from_env()
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SCOPE,
        cache_path=CACHE_PATH,
    ))
