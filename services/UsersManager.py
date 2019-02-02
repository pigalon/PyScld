from flask import g, current_app
from soundcld.SCUserDao import SCUserDao

from ardb.Playlist import Playlist
from ardb.Track import Track
from ardb.PlaylistRepo import PlaylistRepo
from ardb.UserRepo import UserRepo
from ardb.TrackRepo import TrackRepo

from util.ScDbUtil import ScDbUtil

class UsersManager():

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

    def getFollowingsCountFromSC(self, user_id):
        return self.sCUserDao.get(userId=user_id).followings_count

    def getFollowingsFromSC(self, user_id):
        return self.sCUserDao.get_all_followings_from_user(userId=user_id, limit=0)
 
    def getJsonFollowingsFromSC(self, user_id):
        jsonList = []
        list = self.getFollowingsFromSC(user_id=user_id)
        jsonList = ScDbUtil.scUsersToJsonDbUsers(list)
        return jsonList

    def getFollowingsFromDB(self, user_id):
        return self.userRepo.get_by_id(userId=user_id).followings

    def getJsonFollowingsFromDB(self, user_id):
        jsonList = []
        list = self.getFollowingsFromDB(user_id=user_id)
        for user in list :
            jsonList.append(user.to_dict())
        return jsonList
    
   