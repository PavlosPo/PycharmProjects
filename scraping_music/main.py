import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os

url = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? \nType the date in this format YYYY-MM-DD: ")

url_end = url + str(date)

CLIENT_ID = "92fdb96a4f754c86b57cdd7b1cac2fe1"
CLIENT_SECRET = "34819680ca934d7e8158ea34641f9e45"

playlist_name = f"Billboard Top 100 {date}"
description = "Top 100 songs of that time period, based on billboard!"

# Find Artists and Song name from Billboard.com
response = requests.get(url=url_end).text
soup = BeautifulSoup(response, "lxml")
tags = soup.find_all(name="ul",
                     class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")

# Find the songs in the Spotify to add later
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public",
                                               cache_path=".cache",
                                               show_dialog=True))

# user_id = sp.current_user()['id']
# query = f"artist:{artists[0]} track:{songs[0]}"
# results = sp.search(q=query, type='track')
# uri_track = results['tracks']['items'][-1]['uri']

year = date.split("-")[0]  # Takes the Year
songs = [tag.find(name="h3", id="title-of-a-story").getText().strip() for tag in tags]
artists = [tag.find(name="span", class_="c-label").getText().strip() for tag in tags]
user_id = sp.current_user()['id']
uri_tracks = []
for index in range(len(songs)):
    query = f"track:{songs[index]} year:{year}"
    try:
        result = sp.search(q=query, type='track')
        uri_tracks.append(result['tracks']['items'][0]['uri'])
    except:
        print(f"*********\nSong: {songs[index]}\nArtist: {artists[index]}\nDoesn't Exists, Skipped.\n*********")


# Create the playlist to the user
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=description)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_tracks)

