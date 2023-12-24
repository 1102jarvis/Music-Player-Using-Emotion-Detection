import spotipy
import json
import webbrowser
import random

username = '31q2bru3s2yq2t3amuuiy5kygraa'
client_id = 'b198c8bd8a574babbc49616d3b0f46c1'
client_secret_id = 'fbcdc5acddb3490795c007d08c541f4d'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(client_id,client_secret_id,redirect_uri)
token_dict = oauth_object.get_access_token()
print(token_dict)
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)
user_name = spotify_object.current_user()

print(json.dumps(user_name,sort_keys=True, indent=4))

def play_song(song):
  results = spotify_object.search(song,1,0,'track')
  song_dict = results['tracks']
  song_items = song_dict['items']
  if not song_items:
    print('Enter valid song')
    return
  song = song_items[0]['external_urls']['spotify']
  webbrowser.open(song)
  print('Song is opened in the browser')

def play_from_playlist(playlist_uri):
  playlist_tracks = spotify_object.playlist_tracks(playlist_uri)
  random_track = random.choice(playlist_tracks['items'])
  print(random_track)
  song = random_track['track']['external_urls']['spotify']
  webbrowser.open(song)
  print('Song is opened in the browser')