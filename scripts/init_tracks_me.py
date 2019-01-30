from datetime import datetime
import soundcloud

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from arangodb.TrackRepo import TrackRepo

from soundcld.SCUserDao import SCUserDao


clientS = soundcloud.Client(client_id=app.config["APY_KEY"])

moi = clientS.get('/users/pierrock')
print('Mon id : ' + str(moi.id))

ardb = DatabaseAdb()
###############################
sCUserDao = SCUserDao(clientS)
trackRepo = TrackRepo(db=ardb.db)


print("#####################")
# Store all tracks in db
cpt = 0
allTracks = sCUserDao.get_all_tracks_from_user(userId=str(moi.id))
for track in allTracks :
    cpt = cpt + 1
    print(str(cpt) + " add track : " + str(track.id) + " - " + track.title)
    trackRepo.sc_to_db(track=track, ranking=5)
    
    




