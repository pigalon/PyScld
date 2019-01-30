from datetime import datetime
import soundcloud

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from arangodb.TrackRepo import TrackRepo
from soundcld.SCUserDao import SCUserDao
from delta.DeltaCalculator import DeltaCalculator

clientId = app.config["APY_KEY"]
clientS = soundcloud.Client(client_id=clientId)

ardb = DatabaseAdb()

moiSC = clientS.get('/users/pierrock')
print('Mon id : ' + str(moiSC.id))


###############################
sCUserDao = SCUserDao(clientSC=clientS, clientId=clientId)
userRepo = UserRepo(db=ardb.db)
trackRepo = TrackRepo(db=ardb.db)


dc = DeltaCalculator(userRepo=userRepo, sCuserDao=sCUserDao)
dc.calculate_delta_on_first_degree(userId=moiSC.id)


userAR = userRepo.from_db_by_id(userId=str(moiSC.id))


delta = moiSC.public_favorites_count - userAR.public_favorites_count 

print("#####################  delta : " + str(delta) + " - " + str(moiSC.public_favorites_count) + " - " + str(userAR.public_favorites_count ))
# Store all tracks in db
cpt = 0
allFavorites = sCUserDao.get_all_favorites_from_user(userId=str(moiSC.id),limit=delta)

print(" nb tracks : " + str(len(allFavorites))) 
for track in allFavorites :
#    print(str(cpt) + " add track : " + str(track.id) + " - " + track.title)
    trackRepo.sc_to_db(track=track, ranking=5)
    
    




