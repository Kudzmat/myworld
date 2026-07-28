import json

from vibecheck.spotify_utils import get_spotify_client, CACHE_PATH

if __name__ == "__main__":
    sp = get_spotify_client()
    profile = sp.me()
    print(f"Logged in as: {profile['display_name']} ({profile['id']})")

    with open(CACHE_PATH) as f:
        token_info = json.load(f)
    print("\nCopy this into SPOTIPY_REFRESH_TOKEN (local .env and Heroku config vars):")
    print(token_info["refresh_token"])