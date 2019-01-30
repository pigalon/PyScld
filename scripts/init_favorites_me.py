from datetime import datetime

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from arangodb.TrackRepo import TrackRepo

import soundcloud


from soundcld.SCUserDao import SCUserDao


clientS = soundcloud.Client(client_id=app.config["APY_KEY"])

ardb = DatabaseAdb()

moi = clientS.get('/users/pierrock')
print('Mon id : ' + str(moi.id))


###############################
sCUserDao = SCUserDao(clientS)
trackRepo = TrackRepo(db=ardb.db)


print("#####################")
# Store all tracks in db
cpt = 0
allFavorites = sCUserDao.get_all_favorites_from_user(userId=str(moi.id))
for track in allFavorites :
    cpt = cpt + 1
    print(str(cpt) + " add track : " + str(track.id) + " - " + track.title)
    trackRepo.sc_to_db(track=track, ranking=5)
    
    




