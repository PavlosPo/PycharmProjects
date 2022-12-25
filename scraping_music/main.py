import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os

url = "https://www.billboard.com/charts/hot-100/"
date = input("Which year to you want to travel to? \nType the date in this format YYYY-MM-DD: ")
url_end = url + str(date)


playlist_name = "Top 100 songs "
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
                                               scope="playlist-modify-private"))

# user_id = sp.current_user()['id']
# query = f"artist:{artists[0]} track:{songs[0]}"
# results = sp.search(q=query, type='track')
# uri_track = results['tracks']['items'][-1]['uri']

year = date.split("-")[0]  # Takes the Year
songs = [tag.find(name="h3", id="title-of-a-story").getText().strip() for tag in tags]
artists = [tag.find(name="span", class_="c-label").getText().strip() for tag in tags]
user_id = sp.current_user()['id']
uri_track = []
for index in range(len(songs)):
    query = f"track:{songs[index]} year:{year}"
    try:
        result = sp.search(q=query, type='track')
        uri_track.append(result['tracks']['items'][0]['uri'])
    except:
        print(f"*********\nSong: {songs[index]}\nArtist: {artists[index]}\nDoesn't Exists, Skipped.\n*********")
pprint(uri_track)
