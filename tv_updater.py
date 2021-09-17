import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os

with open('.env', 'r') as fh:
    vars_dict = dict(
        tuple(line[:-1].split('='))
        for line in fh.readlines() if not line.startswith('#')
    )
os.environ.update(vars_dict)


scope = "playlist-modify-public playlist-modify-private"
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playlists()
playlists = []
for idx, item in enumerate(results['items']):
    playlists.append(sp.playlist(item['id']))

total = 0
for playlist in playlists:
    to_add_uris = []
    to_remove_ids = []
    tracks = playlist['tracks']['items']
    for item in tracks:
        track = item['track']
        artists = track['artists']
        for artist in artists:
            if artist['name'] == 'Taylor Swift' and 'Version' not in track['name']:
                search_str = track['name'] + ' (Taylor\'s Version)'
                result = sp.search(search_str)['tracks']['items']
                if len(result) != 0:
                    result = result[0]
                    if '(Taylor\'s Version)' in result['name'] or 'Taylor’s Version' in result['name']:
                        to_add_uris.append(result['uri'])
                        to_remove_ids.append(track['id'])
    if len(to_remove_ids) != 0:
        total += len(to_remove_ids)
        sp.playlist_remove_all_occurrences_of_items(playlist['id'], to_remove_ids)
        sp.playlist_add_items(playlist['id'], to_add_uris)


print(f'Total tracks changed: {total}')


