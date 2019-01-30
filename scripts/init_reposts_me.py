from datetime import datetime
import soundcloud

# LOCAL IMPORTS
from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.TrackRepo import TrackRepo
from soundcld.SCUserDao import SCUserDao

clientId = app.config["APY_KEY"]
clientS = soundcloud.Client(client_id=clientId)

ardb = DatabaseAdb()

moi = clientS.get('/users/pierrock')
print('Mon id : ' + str(moi.id))

###############################
    
sCUserDao = SCUserDao(clientSC=clientS, clientId=clientId)
trackRepo = TrackRepo(db=ardb.db)


reposts = sCUserDao.get_all_reposts_from_user(userId=moi.id)
trackRepo.write_list(allTracks=reposts, ranking=5)   
    




