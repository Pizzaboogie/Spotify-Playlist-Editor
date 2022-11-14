
#!sop=songs of playlist,plid=playlist id
ids=[]
import spotipy
from spotipy import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a2165466c9f144d29c113c15eb89f7f7",
    client_secret="287e7dc735e44bb4b74ade6afc4e4fe2",
    redirect_uri="http://localhost:8080" ,
    scope = "playlist-read-private playlist-modify-private playlist-modify-public",
    show_dialog=True))

user_id=sp.current_user()['id']
print(user_id)

def printline(gap=False):
    print("---------------------------")
    if gap==True:
        print("")

def printall(sp,ids):
    print("ALL YOUR PLAYLISTS")
    print("SN | NAME OF PLAYLIST\n---------------------------")
    results=sp.current_user_playlists()
    #for x in results['items']:
       # if x['owner']['id']!=user_id:
            #results['items'].pop(x)
    #print(i['name'] for i in results['items'])
    for num,i in enumerate(results['items']):
        if num<9:gap='  '
        elif num<100:gap=' '
        else:gap=''
        print (num+1,gap,'| ',i['name'],sep='')
        ids.append(i['id'])
    return results
    

def selectplaylist(ids,results):
    printline()
    global ch
    ch=int(input("enter SN of playlist to modify: "))-1
    #viewing individual playlist
    playlist_id=ids[ch]
    print((results['items'][ch]['name']).upper())
    return playlist_id

def displaysop(playlist_id):
    songs_of_playlist,mod,x=[],[],0
    #print((results['items'][ch]['name']).upper())
    printline()
    for x in range(0,1000,100):
        mod.extend(sp.playlist_items(playlist_id,fields='items.track.name,total',offset=x,additional_types=['track'])['items'])
    for n,x in enumerate(mod):
        print (n+1,'.',x['track']['name'].upper())
        songs_of_playlist.append(x['track']['name'].upper())
    return (songs_of_playlist)

def displaysop2(playlist_id):
    songs_of_playlist=sp.playlist_items(playlist_id,fields='items.track.name,total',additional_types=['track'])['items'][0]['track']['name']
    return songs_of_playlist

def addsongs(plid,ids):
    song_id=[]
    sea=input("Enter song to be added:")
    search_results=sp.search(sea,limit=1,type="track")
    song_id.append(search_results['tracks']['items'][0]['id'])
    sp.playlist_add_items(plid,song_id, position=None)
    print(sea,'has been added successfully!')
        
def remove(plid):
    sop=displaysop(plid)
    while 1:
        songnums=list(eval(input("enter SN of the songs to delete (example:-2,5,6 or 15-20):")+','))
        #print(songnums)
        for i in songnums:
            if i>len(sop):
                print("Incorrect SN value inputted!")
            else:break
        break
    songids=[]
    for num in songnums:
        if num>100:
            x=100*(num//100)
            num=num%100
        else:x=0
        songids.append(sp.playlist_tracks(plid, fields=None,offset=x, additional_types=('track',))['items'][num-1]['track']['id'])
    #sp.playlist_tracks('plid', fields=None, additional_types=('track',))['items']['track']['id']:   
    sp.playlist_remove_all_occurrences_of_items(plid,songids) 

def main():
    printline()
    print("SPOTIFY PLAYLIST EDITOR")
    printline()
    results=printall(sp,ids)
    plid=selectplaylist(ids,results)
    choice=int(input("1.Add Song\n2.Remove Song/Songs\n->"))
    if choice==1:addsongs(plid,ids)
    if choice==2:remove(plid)   

main()
#todo start the reorder algorithm, take range of songs to del