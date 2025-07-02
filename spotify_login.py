from vibecheck.spotify_utils import get_spotify_client

if __name__ == "__main__":
    sp = get_spotify_client()
    profile = sp.me()
    print(f"Logged in as: {profile['display_name']} ({profile['id']})")