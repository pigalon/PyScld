from arango import ArangoClient
from arango_orm import Database

from datetime import datetime

from Track import Track

from TrackRepo import TrackRepo

import soundcloud

clientS = soundcloud.Client(client_id=app.config["APY_KEY"])
tracky = clientS.get('/tracks/347632577')
# 

client = ArangoClient(protocol='http', host='localhost', port=8529)
test_db = client.db('soundcloud', username='root', password='')

db = Database(test_db)

trackRepo = TrackRepo(db=db)
trackRepo.write(tracky)


#t = Track()
#t = Track(title='test', _key='12311', genre='pop', created_at=datetime(year=2016, month=9, day=12, hour=20, minute=30, second=10))
#t.convert(soundcloudTrack=tracky)
#db.add(t)


#print(t.title)
