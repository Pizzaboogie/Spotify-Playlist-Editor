

#!sop=songs of playlist,plid=playlist id
ids=[]
import spotipy
from spotipy import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="***USE YOUR CLIENT ID HERE***",
    client_secret="***USE YOUR CLIENT SECRET HERE",
    redirect_uri="http://localhost:8080" ,
    scope = "playlist-read-private playlist-modify-private playlist-read-collaborative playlist-modify-public"))
#playlist-read-private playlist-modify-private playlist-read-collaborative
user_id=sp.current_user()['id']
print(user_id)
results=sp.current_user_playlists()
def printline(gap=False):
    print("---------------------------")
    if gap==True:
        print("")

def printall(sp=sp):
    results=sp.current_user_playlists()
    nop,idop,toremove=[],[],[]
    for num,x in enumerate(results['items']):
        if x['owner']['id']!=user_id:
            toremove.append(num)
    for num,i in enumerate(results['items']):
        if num not in toremove:
            nop.append(i['name'])
            idop.append(i['id'])
    return nop,idop

#! i found it!
def reorder(plid):
    #playlist_reorder_items
    sop=displaysop(plid)
    print(sop)
    
    

def selectplaylist(choice,results=results):
    global ch
    #ch=int(input("enter SN of playlist to modify: "))-1
    nop,idop=printall()
    playlist_id=idop[choice]
    #print((results['items'][ch]['name']).upper())
    return playlist_id

def displaysop(playlist_id):
    songs_of_playlist,mod,x=[],[],0
    #print((results['items'][ch]['name']).upper())
    
    for x in range(0,1000,100):
        mod.extend(sp.playlist_items(playlist_id,fields='items.track.name,total',offset=x,additional_types=['track'])['items'])
    for n,x in enumerate(mod):
        #print (n+1,'.',x['track']['name'].upper())
        songs_of_playlist.append(x['track']['name'].upper())
    return (songs_of_playlist)

def displaysop2(playlist_id):
    songs_of_playlist=sp.playlist_items(playlist_id,fields='items.track.name,total',additional_types=['track'])['items'][0]['track']['name']
    return songs_of_playlist

def addsongs(plid):
    song_id=[]
    sea=input("Enter song to be added:")
    search_results=sp.search(sea,limit=1,type="track")
    song_id.append(search_results['tracks']['items'][0]['id'])
    sp.playlist_add_items(plid,song_id, position=None)
    #print(sea,'has been added successfully!')
        
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
    #print(sop[(x+num)-1],'has been successfully deleted!')

def main():
    
    plid=selectplaylist()
    while 1:
        choice=int(input("1.Add Song\n2.Remove Song/Songs\n3.Change playlist\n4.Exit\n->"))
        if choice==1:addsongs(plid)
        elif choice==2:remove(plid)   
        elif choice==3:main()
        elif choice==4:break
        else:print("enter valid option")
plid=selectplaylist(int(input('')))
reorder(plid)
