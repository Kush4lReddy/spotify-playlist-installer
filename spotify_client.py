import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config


def getSongs(playlist_ID):
    
    spotify_Obj = spotipy.Spotify(auth_manager=SpotifyClientCredentials( 
        client_id = config.SPOTIFY_CLIENT_ID,
        client_secret = config.SPOTIFY_CLIENT_SECRET )) # Authenticate using credentials from config.py
    
    songs_data = []

    playlist = spotify_Obj.playlist_items(playlist_ID) # Get playlist details
    for id, item in enumerate(playlist['items']):
        track = item['track']
        songs_data.append({
            'Song Name': track['name'],
            'Artists': track['artists'][0]['name']  # Join multiple artists with a comma
        })
        print(id, track['artists'][0]['name'], " – ", track['name'])

    return songs_data
