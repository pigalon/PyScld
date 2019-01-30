from arango import ArangoClient
from arango_orm import Database

from datetime import datetime

from User import User

from UserRepo import UserRepo

import soundcloud


clientS = soundcloud.Client(client_id=app.config["APY_KEY"])


client = ArangoClient(protocol='http', host='localhost', port=8529)
test_db = client.db('soundcloud', username='root', password='')

db = Database(test_db)



user = clientS.get('/users/pierrock')
print(user.id)

userRepo = UserRepo(db=db)

#userRepo.sc_to_db(user)

#userObj = userRepo.from_db_by_id(str(user.id))
userObj = userRepo.from_db_by_username(user.username)
userObj.display()


#clientS.get('/users/'+str(user.id)+'/playlists')
pgsize=10
playlists = clientS.get('/users/21381146/playlists' , limit=pgsize)

for playlist in playlists :
    print(str(playlist.id) + " - " + playlist.title)

try:
       while playlists.next_href != None:
            playlists = client.get(playlists.next_href , limit=pgsize, order='id',
                linked_partitioning=1)
            for playlist in playlists :
                print(str(playlist.id) + " - " + playlist.title)


except AttributeError as e:
            print('Exception found!: ' + str(e))


#db = Database(test_db)

#trackRepo = TrackRepo(db=db)
#trackRepo.write(tracky)


#t = Track()
#t = Track(title='test', _key='12311', genre='pop', created_at=datetime(year=2016, month=9, day=12, hour=20, minute=30, second=10))
#t.convert(soundcloudTrack=tracky)
#db.add(t)


#print(t.title)
