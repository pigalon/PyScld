from datetime import datetime

from arangodb.DatabaseAdb import DatabaseAdb
from arangodb.User import User
from arangodb.UserRepo import UserRepo
from arangodb.TrackRepo import TrackRepo

import soundcloud


from soundcld.SCUserDao import SCUserDao

clientId = app.config["APY_KEY"]
clientS = soundcloud.Client(client_id=clientId)

ardb = DatabaseAdb()


moi = clientS.get('/users/pierrock')
print('Mon id : ' + str(moi.id))

userRepo = UserRepo(db=ardb.db)

u= User()
u.convert(soundcloudUser=moi)
u.degree = 0
u.dt_bd_action=datetime.today()

userRepo.write(u)




