import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
        client_id="daee064121c042429033426b80cfacde",
        client_secret="4fe548d57d3940a3bb0245f7d82d7495")

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

#playlists = spotify.user_playlists('alexfloo7')
topMexico = spotify.search("Mexico Top 50", offset=1, type='playlist')
actualPlaylist={}

actualPlaylist = {key:value for key, value in topMexico['playlists']['items'][0].items()}
print(actualPlaylist)
tracks = spotify.user_playlist_tracks('spotify',actualPlaylist['id'])
print(tracks)
#while playlists:
    #for i, playlist in enumerate(playlists['items']):
      #  print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
   # if playlists['next']:
    #    playlists = spotify.next(playlists)
   # else:
    #    playlists = None

