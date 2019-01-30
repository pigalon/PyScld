from datetime import datetime

import soundcloud

from ardb.DatabaseAdb import DatabaseAdb
from soundcld.SCUserDao import SCUserDao
from ardb.TrackRepo import TrackRepo
from ardb.Track import Track
from ardb.Playlist import Playlist
from ardb.PlaylistRepo import PlaylistRepo


clientS = soundcloud.Client(client_id=app.config["APY_KEY"])

ardb = DatabaseAdb()


moi = clientS.get('/users/pierrock')
print('Mon id : ' + str(moi.id))


###############################
# Get PLaylists

trackRepo = TrackRepo(db=ardb.db)
playlistRepo = PlaylistRepo(db=ardb.db)
sCUserDao = SCUserDao(clientSC=clientS, clientId=moi.id)

cpt_added = 0
cpt_canceled = 0

playlistsComplete = sCUserDao.get_all_playlists_from_user(userId=str(moi.id))
for playlist in playlistsComplete :
    print(str(playlist.id) + " - " + playlist.title)
    p = Playlist()
    p.convert(soundcloudPlaylist=playlist)
    if (playlistRepo.write(playlist=p, ranking=5)) : 
        cpt_added = cpt_added + 1
        print("added cpt : " + str(cpt_added))
    else :
        cpt_canceled = cpt_canceled + 1
        print("canceled cpt : " + str(cpt_canceled))

##################################

    for track in playlist.tracks :
        print("track : " + str(track["id"]) + " - " + track["title"])
        t= Track()
        t.convert_from_json_playlis(soundcloudTrack=track)
        if (trackRepo.write(track=t, ranking=5)) : 
            cpt_added = cpt_added + 1
            print("added cpt : " + str(cpt_added))
        else :
            cpt_canceled = cpt_canceled + 1
            print("canceled cpt : " + str(cpt_canceled))


print("#####################")
# Store all tracks in db

#for track in allFavorites :
#    print("track : " + str(track.id) + " - " + track.title)
    


#playlistsComplete = []
#pgsize=10
#playlists = clientS.get('/users/'+str(moi.id)+'/playlists' , limit=pgsize, linked_partitioning=1)




#try:
#       while playlists.next_href != None:
#            playlists = clientS.get(playlists.next_href , limit=pgsize)
#            for playlist in playlists.collection :
#                playlistsComplete.append(playlist)

#except AttributeError as e:
#            print('Exception found!: ' + str(e))


