from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = [
    "user-library-read",
    "user-read-currently-playing",
    "user-read-recently-played",
    "user-top-read",
]


def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.currently_playing()
    print(results["item"]["name"])
    results = sp.current_user_recently_played(limit=2)
    for song in results["items"]:
        print(song["track"]["name"])

    results = sp.current_user_top_tracks(time_range="short_term", limit=2)
    for song in results["items"]:
        print(song["name"])

    results = sp.current_user_top_tracks(time_range="medium_term", limit=2)
    for song in results["items"]:
        print(song["name"])

    results = sp.current_user_top_tracks(time_range="long_term", limit=2)
    for song in results["items"]:
        print(song["name"])

    results = sp.current_user_top_artists(time_range="short_term", limit=2)
    for artist in results["items"]:
        print(artist["name"])

    results = sp.current_user_top_artists(time_range="medium_term", limit=2)
    for artist in results["items"]:
        print(artist["name"])

    results = sp.current_user_top_artists(time_range="long_term", limit=2)
    for artist in results["items"]:
        print(artist["name"])


if __name__ == "__main__":
    main()
