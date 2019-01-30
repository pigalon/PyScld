import soundcloud

from datetime import datetime

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from arangodb.Playlist import Playlist
from arangodb.PlaylistRepo import PlaylistRepo
from arangodb.Track import Track
from arangodb.TrackRepo import TrackRepo


from soundcld.SCUserDao import SCUserDao
from soundcld.SCPlaylistDao import SCPlaylistDao

clientId = app.config["APY_KEY"]
clientSC = soundcloud.Client(client_id=clientId)

ardb = DatabaseAdb()


userRepo = UserRepo(db=ardb.db)
sCUserDao =SCUserDao(clientSC=clientSC, clientId=clientId)

users = userRepo.get_all_first_degree()

cpt = 0
for user in users:
    print(str(cpt) + " - user : + " + str(user._key))
    cpt = cpt + 1
        
 #   favorites = sCUserDao.get_all_favorites_from_user(userId=user._key, limit=0)
    #print("favorites nb : + " + str(len(favorites)))
 #   for favorite in favorites :
 #       print("favorite : " + favorite.title)

 #   tracks = sCUserDao.get_all_tracks_from_user(userId=user._key)
    #print("tracks nb : + " + str(len(tracks)))
 #   for track in tracks :
 #       print("track : " + track.title)

 #   reposts = sCUserDao.get_all_reposts_from_user(userId=user._key)
    #print("reposts :::: " + str(reposts))
#    for track in reposts :
#        if track is not None and track.title is not None :
#            print("repost : " + str(track.title))
    sCPlaylistDao = SCPlaylistDao(clientSC=clientSC)
    playlistRepo = PlaylistRepo(db=ardb.db)
    playlists = sCUserDao.get_all_playlists(userId=user._key)

    convertedPlaylists = sCPlaylistDao.getAllConvertedPlaylist(playlists)
    playlistRepo.writeList(convertedPlaylists, 4)
    
    for playlist in playlists :
        print(str(playlist.id) + " - " + playlist.title)
#        
#        p = Playlist()
#        p.convert(soundcloudPlaylist=playlist)
#        if (playlistRepo.write(playlist=p, ranking=4)) : 
#            cpt_added = cpt_added + 1
#            print("added cpt : " + str(cpt_added))
#        else :
#            cpt_canceled = cpt_canceled + 1
#            print("canceled cpt : " + str(cpt_canceled))

    ##################################
        tracks = sCPlaylistDao.getAllConvertedTracks(playlist)
        for track in tracks :
            print("track : " + str(track._key) + " - " + track.title)
 #           print("track : " + str(track["id"]) + " - " + track["title"])
 #           t= Track()
 #           t.convert_from_json_playlis(soundcloudTrack=track)
 #           if (trackRepo.write(track=t, ranking=5)) : 
 #               cpt_added = cpt_added + 1
 #               print("added cpt : " + str(cpt_added))
 #           else :
 #               cpt_canceled = cpt_canceled + 1
 #               print("canceled cpt : " + str(cpt_canceled))



    if cpt > 4 :
        break 
    







