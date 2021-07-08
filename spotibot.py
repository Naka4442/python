import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid    = "b55102c9b89c445f9895e6ad6f4741cb"
secret = "f6ba452b9f3c4199963679e067a949b9"
client_credentials = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)
def findTracks(name, limit=10):
    tracks = sp.search(q=name, limit=limit, type="track")["tracks"]["items"]
    for track in tracks:
        print(track["album"]["artists"][0]["name"] + " - " + track["name"])