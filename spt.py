import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Authentication
scope = "playlist-modify-public,playlist-modify-private,playlist-read-private,playlist-read-collaborative"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#Variables
pl_id=''
user=sp.me()

#Get User Mood
print("\nHello!\nLets make a playlist just for you!\nRate the following parameters on 0-100 based on how much would u like them in the songs.\n")
ener=(int(input("Energy: ")))/100
danc=(int(input("Dancability: ")))/100
arco=(int(input("Arcoustic: ")))/100
inst=(int(input("Instrumental: ")))/100
popu=int(input("Popularity: "))

s_seed=input("\nInsert a song link for the seed: ")
a_seed=''
g_seed=''
sng = sp.track(s_seed, market=None)
for idx, item in enumerate(sng['artists']):
    a_seed = item['id']
art = sp.artist(a_seed)
for idx, item in enumerate(art['genres']):
    g_seed = item

la=[a_seed]
lg=[g_seed] 
ls=[s_seed]

rec = sp.recommendations(seed_artists=la, seed_genres=lg,seed_tracks=ls, limit=50, country=None,
                         target_acousticness=arco, target_danceability=danc, target_energy=ener, target_instrumentalness=inst, target_popularity=popu)

i=1
print("\n\nSong List:")
for idx, item in enumerate(rec['tracks']):
    print(i,") ",item["name"])
    i+=1

pl_name = input("\nTo finish the process give the playlist a name: ")
sp.user_playlist_create(user["id"], pl_name, public=False, collaborative=False, description='')
results= sp.current_user_playlists(limit=1, offset=0)
for idx, item in enumerate(results['items']):
    pl_id = item['id']

for idx, item in enumerate(rec['tracks']):
    sp.playlist_add_items(pl_id, [item["uri"]], position=None)

