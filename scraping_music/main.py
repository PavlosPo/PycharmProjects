import spotipy
from spotipy.oauth2 import SpotifyOAuth


url = "https://www.billboard.com/charts/hot-100/"
date = input("Which year to you want to travel to? \nType the date in this format YYYY-MM-DD: ")
url_end = url + str(date)
CLIENT_ID = "92fdb96a4f754c86b57cdd7b1cac2fe1"
CLIENT_SECRET = "34819680ca934d7e8158ea34641f9e45"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

results = sp.current_user()
print(results)