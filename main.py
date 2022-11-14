
ids=[]
import spotipy
from spotipy import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="***USE YOUR CLIENT ID***",
    client_secret="***USE YOUR CLIENT SECRET ID***",
    redirect_uri="http://localhost:8080" ,
    scope = "playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative user-top-read"))
'''
results=sp.current_user_playlists()
for i in results['items']:
    print (i['name'])
    print(i['id'])
'''
def printline(gap=False):
    print("---------------------------")
    if gap==True:
        print("")
def printall(sp,ids):
    print("ALL PLAYLISTS")
    printline()
    results=sp.current_user_playlists()
    for num,i in enumerate(results['items']):
        print (num+1,'. ',i['name'],sep='')
        ids.append(i['id'])
    return results
    

def selectplaylist(ids,results):
    printline()
    global ch
    ch=int(input("enter playlist to view/modify: "))-1
    #viewing individual playlist
    playlist_id=ids[ch]
    print((results['items'][ch]['name']).upper())
    printline()
    mod=sp.playlist_items(playlist_id,fields='items.track.name,total',additional_types=['track'])
    for x in mod['items']:
        print ((x['track']['name']).upper())
    return playlist_id

    
def addsongs(plid,ids):
    song_id=[]
    sea=input("Enter song to be added:")
    search_results=sp.search(sea,limit=1,type="track")
    song_id.append(search_results['tracks']['items'][0]['id'])
    sp.playlist_add_items(plid,song_id, position=None)
    print(song_id)
        
def reordersongs(plid):
    sp.playlist_remove_all_occurrences_of_items(plid,items) 

results=printall(sp,ids)
plid=selectplaylist(ids,results)
addsongs(plid,ids)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
# print(sp.current_user_playing_track()['item']['name'],sp.current_user_playing_track()['item']['artists'][0]['name'],sep=' by ')
'''for i in range(6):
    for x in sp.current_user_saved_tracks(limit=50,offset=i*50)['items']:
        print(x['track']['name'])
'''

