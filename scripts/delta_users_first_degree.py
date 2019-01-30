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

# Delta on my first degree => add missing user
dc = DeltaCalculator(userRepo=userRepo, sCuserDao=sCUserDao)
dc.calculate_delta_on_first_degree(userId=moiSC.id)

# get all first degree user
followings = userRepo.get_all_first_degree()

for following in followings :
    print("user : " + following.username +" - " + str(following._key))
    dc.calculate_delta_on_first_degree(userId=following._key)
