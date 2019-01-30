import soundcloud

import rx
from rx import Observable, Observer

import json

from datetime import datetime

from pyArango.connection import *
conn = Connection(username="root", password="")

db = conn["soundcloud"]

#trakcsCollection = db.createCollection(name="Tracks")
trakcsCollection = db["Tracks"]

#track1 = trakcsCollection.createDocument()

track1 = trakcsCollection["2148402"]


print("track1 : " + track1["title"])

#track1["id"] = 1
#track1["title"] = "test"
#track1.save()
 
# #### Souncloud attributes
# kind
# id
# created_at
# user_id
# duration
# commentable : True / false



#import MyObserver

client = soundcloud.Client(client_id='app.config["APY_KEY"]')



#tracks = client.get('/tracks', limit=10)
#for track in tracks:
#    print track.title

#playlists = client.get('/users/21381146/playlists' , limit=10)
#for playlist in playlists:
#    print ("{0} : {1} ", playlist.id, playlist.title)
#    tracks = client.get('/playlists/' + str(playlist.id) + '/tracks/' , limit=10)
#    for track in tracks:
#        print ("{0}", track.title)



app = client.get('/users/propellerrecordings')
print(app.id)


# start paging through results, 100 at a time
#tracks = client.get('/users/1158174/tracks', order='created_at', limit=100,
#                    linked_partitioning=1)
#for track in tracks:
#    print track.title
pgsize=100
tracks = client.get('/users/1158174/tracks' , limit=pgsize, order='id',
                   linked_partitioning=1)

tracky = client.get('/tracks/522754050')


dt = datetime.strptime(tracky.created_at, '%Y/%m/%d %H:%M:%S %z')
print("!!!!!!! " + str(dt.year))

#track = client.get('/tracks/290')
#print("tracky!!! " + track.id)
cpt=0
#tracky = next(iter(tracks.collection), 4)
#print ("track y " + tracky.genre)
#attrs = vars(tracky('obj')
#attrs = [attr for attr in dir(tracky.obj) 
#              if not attr.startswith('__')]
#print (', '.join("%s: %s" % item for item in attrs.items()))

#########################
for attr in dir(tracky):
    if attr == "obj":
              print("{")
              for item in getattr(tracky, attr) :
                  print("  "+ item +" : "+ str(getattr(tracky, item)))
              print("}")
#########################@@
# pretty printing of json-formatted string
#print (json.dumps(decoded, sort_keys=True, indent=4))


for track in tracks.collection:
       cpt = cpt + 1
       print ("track n" + str(cpt) + " : id ="+ str(track.id)  +" -genre = " + track.genre + " -tags= "+ track.tag_list)
       #attrs = vars(track)
       #print (', '.join("%s: %s" % item for item in attrs.items()))
       

try:
       while tracks.next_href != None:
              tracks = client.get(tracks.next_href , limit=pgsize, order='id',
                   linked_partitioning=1)
              #for track in tracks.collection:
              #       cpt = cpt + 1
              #      print ("track n" + str(cpt) + " : " + track.title)


except AttributeError as e:
            print('Exception found!: ' + str(e))

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

xs = Observable.from_(tracks)
xs.subscribe(MyObserver())


#tracks = tracks.next_href
#for track in tracks:
#       print ("track : " + track.title)




#tracks = client.get('/users/1158174/favorites' , limit=100)
#for track in tracks:
#       print ("favorite : " +  track.title)