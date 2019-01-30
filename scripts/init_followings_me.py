import soundcloud
from datetime import datetime

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from soundcld.SCUserDao import SCUserDao


clientId = app.config["APY_KEY"]
clientSC = soundcloud.Client(client_id=clientId)

ardb = DatabaseAdb()

userRepo = UserRepo(db=ardb.db)
moi = clientSC.get('/users/pierrock')
print('Mon id : ' + str(moi.id))

sCUserDao = SCUserDao(clientSC=clientSC, clientId=moi.id)

cpt_added = 0
cpt_canceled = 0

followingsComplete = sCUserDao.get_all_followings_from_user(userId=str(moi.id),limit=0)
userRepo.change_degree_for_a_list(followingsComplete,2)
print(followingsComplete[1].username)
userRepo.write_user_list(followingsComplete)
