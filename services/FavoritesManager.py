from flask import g, current_app
from soundcld.SCUserDao import SCUserDao
from ardb.UserRepo import UserRepo

class FavoritesManager():

    sCUserDao = None
    userRepo = None


    def __init__(self):
        client_sc = getattr(g,'client_sc', None)
        db = getattr(g,'db', None)
        self.sCUserDao = SCUserDao(clientSC=client_sc, clientId='')
        self.userRepo = UserRepo(db=db)


    def getFavoritesCountFromSCUser(self, user_id):
        return self.sCUserDao.get(user_id).public_favorites_count

    def getFavoritesCountFromBDUser(self, user_id):
        return self.userRepo.get_by_id(userId=user_id).public_favorites_count

    def getFavoritesCountDelta(self, user_id):
        return (self.getFavoritesCountFromSCUser(user_id=user_id) - self.getFavoritesCountFromBDUser(user_id=user_id))

    