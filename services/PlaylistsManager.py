from flask import g, current_app
from soundcld.SCUserDao import SCUserDao

from ardb.Playlist import Playlist
from ardb.Track import Track
from ardb.PlaylistRepo import PlaylistRepo
from ardb.UserRepo import UserRepo
from ardb.TrackRepo import TrackRepo

class PlaylistsManager():

    sCUserDao = None
    trackRepo = None
    playlistRepo = None
    userRepo = None

    def __init__(self):
        client_sc = getattr(g,'client_sc', None)
        self.sCUserDao = SCUserDao(clientSC=client_sc, clientId='')
        
        db = getattr(g,'db', None)
        self.trackRepo = TrackRepo(db=db)
        self.playlistRepo = PlaylistRepo(db=db)
        self.userRepo = UserRepo(db=db)

    def getPlaylistsCountFromSCUser(self, user_id):
        return self.sCUserDao.get(userId=user_id).playlist_count
    
    def getPlaylistsCountFromDB(self, user_id):
        return self.userRepo.get_by_id(userId=user_id).playlist_count

    def getPlaylistsFromSCUser(self, user_id):
        return self.sCUserDao.get_all_playlists(userId=user_id)

    def getPlaylistsFromDB(self, user_id):
        return self.playlistRepo.get_list_by_user_id(user_id=user_id)

    def getJsonPlayslistFromDB(self, user_id):
        jsonList = []
        list = self.getPlaylistsFromDB(user_id=user_id)
        for playlist in list :
            jsonList.append(playlist.to_dict())
        return jsonList
        
        

    def savePlaylists(self, playlistsComplete):

        cpt_added = 0
        cpt_canceled = 0
        
        for playlist in playlistsComplete :
            print(str(playlist.id) + " - " + playlist.title)
            p = Playlist()
            p.convert(soundcloudPlaylist=playlist)
            if (self.playlistRepo.write(playlist=p, ranking=5)) : 
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
            if (self.trackRepo.write(track=t, ranking=5)) : 
                cpt_added = cpt_added + 1
                print("added cpt : " + str(cpt_added))
            else :
                cpt_canceled = cpt_canceled + 1
                print("canceled cpt : " + str(cpt_canceled))

