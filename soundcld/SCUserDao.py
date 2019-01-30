
from soundcld.SCTrackDao  import SCTrackDao
#from arangodb.Track import Track
#from arangodb.User import User
from datetime import datetime

import json, urllib.request

class SCUserDao():

    # Constructor
    def __init__(self, clientSC, clientId):
        self.clientSC = clientSC
        self.clientId = clientId
    
    # get user sc obj
    def get(self, userId):
        return self.clientSC.get('/users/'+str(userId))

    def get_pgsize_from_limit(self, limit):
        if limit > 50 or limit == 0 :
            pgsize = 50
        else :
            pgsize = limit
        return pgsize

##########################   
    def get_all_playlists(self, userId):
        playlistsComplete = []
        pgsize=10
        playlists = self.clientSC.get('/users/'+str(userId)+'/playlists' , limit=pgsize, linked_partitioning=1)

        for playlist in playlists.collection :
            print(str(playlist.id) + " - " + playlist.title)
            playlistsComplete.append(playlist)

        try:
            while playlists.next_href != None:
                    playlists = self.clientSC.get(playlists.next_href , limit=pgsize)
                    for playlist in playlists.collection :
                        print("!!!"+str(playlist.id) + " - " + playlist.title)
                        playlistsComplete.append(playlist)

        except AttributeError as e:
                    print('EOS!: ' + str(e))

        return playlistsComplete

##########################   
    def get_all_favorites_from_user(self, userId, limit):
        allFavorites = []
        pgsize=10
        cpt=0
        tracks = self.clientSC.get('/users/'+str(userId)+'/favorites' , limit=pgsize, linked_partitioning=1)

        for track in tracks.collection :
            if limit!=0 and limit <= len(allFavorites) :
                return allFavorites
            cpt = cpt + 1
            print("n " + str(len(allFavorites)) + " : "  + str(track.id) + " - " + track.title)
            allFavorites.append(track)

        try:
            while tracks.next_href != None:
                    tracks = self.clientSC.get(tracks.next_href , limit=pgsize)
                    for track in tracks.collection :
                        if limit!=0 and limit <= len(allFavorites) :
                            return allFavorites
                        cpt = cpt + 1
                        print("n " + str(len(allFavorites)) + " : "  + str(track.id) + " - " + track.title)
                        allFavorites.append(track)

        except AttributeError as e:
                    print('EOS!: ' + str(e))

        return allFavorites

##########################   
    def get_all_tracks_from_user(self, userId):
        allTracks = []
        pgsize=10
        cpt=0
        tracks = self.clientSC.get('/users/'+str(userId)+'/tracks' , limit=pgsize, linked_partitioning=1)

        for track in tracks.collection :
            cpt = cpt + 1
            print("n " + str(cpt) + " : "  + str(track.id) + " - " + track.title)
            allTracks.append(track)

        try:
            while tracks.next_href != None:
                    tracks = self.clientSC.get(tracks.next_href , limit=pgsize)
                    for track in tracks.collection :
                        cpt = cpt + 1
                        print("n " + str(cpt) + " : "  + "!!!"+str(track.id) + " - " + track.title)
                        allTracks.append(track)

        except AttributeError as e:
                    print('EOS!: ' + str(e))

        return allTracks

##########################
    def get_all_reposts_from_user(self, userId):
     
        url = self.create_repost_url(limit=100, userId=str(userId), offset=0)
    
        completeTracksList = []

        while(url is not None):
            allTracks, url = self.get_some_reposts_from_user(url)
            # add tracks
            completeTracksList.extend(allTracks)
        
        return completeTracksList

##########################   
    def create_repost_url(self, limit, userId, offset):
        return "https://api-v2.soundcloud.com/stream/users/"+str(userId)+"/reposts?limit="+str(limit)+"&offset="+str(offset)+"&client_id="+self.clientId
 
 ##########################
    def get_some_reposts_from_user(self, url):
        reposts = json.loads(urllib.request.urlopen(url).read())
        
        tracks = []
        cpt = 0

        for item in list(reposts["collection"]):
            print("#################################################")
            if(item["type"] == "track-repost") :
                print("value : " + str(item["track"]["id"]))  
#                t= Track()
                
#                t.convert_from_json(soundcloudTrack=item["track"])
#                print("cpt : " + str(cpt) + " - " + self.clientId + " t : " + str(t.title))
#                tracks.append(t)
                cpt = cpt + 1
                

        if reposts["next_href"] is None :
            return tracks, None

        return tracks, reposts["next_href"]+"&client_id="+self.clientId

 ##########################   
    def get_all_followings_from_user(self, userId, limit):
        followingsComplete = []

        pgsize=self.get_pgsize_from_limit(limit)
        
        followings = self.clientSC.get('/users/'+str(userId)+'/followings' , limit=pgsize, linked_partitioning=1)

        for following in followings.collection :
            followingsComplete.append(self.create_user_to_db(following))

        try:
            while followings.next_href != None and (limit == 0 or len(followingsComplete)<limit) :
                    followings = self.clientSC.get(followings.next_href , limit=pgsize)
                    for following in followings.collection :
                        followingsComplete.append(self.create_user_to_db(following))

        except AttributeError as e:
                    print('EOS!: ' + str(e))

        return followingsComplete   

##########################   
    def get_all_followers_from_user(self, userId, limit):
        followersComplete = []
        pgsize=self.get_pgsize_from_limit(limit)
        
        followers = self.clientSC.get('/users/'+str(userId)+'/followers' , limit=pgsize, linked_partitioning=1)

        for follower in followers.collection :
            followersComplete.append(self.create_user_to_db(follower))
        try:
            while followers.next_href != None and (limit == 0 or len(followersComplete)<limit) :
                    followers = self.clientSC.get(followers.next_href , limit=pgsize)
#                    for follower in followers.collection :
#                        followersComplete.append(self.create_user_to_db(follower))

        except AttributeError as e:
                    print('EOS!: ' + str(e))

        return followersComplete

######################################
#    def create_user_to_db(self, scUser):
#        u = User()
#        u.convert(soundcloudUser=scUser)
#        u.dt_bd_action=datetime.today()
#        return u

######################################
    #def create_playlist_to_db(self, scPlaylist, degree):
    #    p = Playlist()
    #    p.convert(soundcloudPlaylist=scPlaylist)
    #    p.degree=degree
    #    p.dt_bd_action=datetime.today()
    #    return p
    