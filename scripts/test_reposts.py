import soundcloud
import json, urllib.request

#import sys, os
#scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
#os.chdir(scriptPath)

#append the relative location you want to import from
#sys.path.append("./arangodb/")

from arangodb.Track import Track
from soundcld.SCTrackDao import SCTrackDao



def get_reposts(clientId, limit, userId):
    url = "https://api-v2.soundcloud.com/stream/users/"+userId+"/reposts?limit="+str(limit)+"&offset=0&client_id="+clientId
    return urllib.request.urlopen(url).read()


clientSC = soundcloud.Client(client_id=app.config["APY_KEY"])

offset = 0
limit = 1

print("offset : " + str(offset))
reposts = json.loads(get_data(limit=limit))

for item in list(reposts["collection"]):
    print ("item : " + str(item))
    print("#################################################")
    #if(item == 'track-repost'):
    #for value in dict.items(item["track"]["id"]):
    print("value : " + str(item["track"]["id"]))
        #print ("key : " + str(key) +" - value : " + str(value))
    dao = SCTrackDao(clientSC=clientSC)   
    tsc = dao.get(item["track"]["id"])
    print("tttt : " + str(tsc.id))
    t= Track()
    t.convert(soundcloudTrack=tsc)
    #t.convert_from_json(soundcloudTrack=item["track"])  

    print("t : " + str(t._key))


#while(reposts["next_href"] != None) :
#    print("next:"+str(reposts["next_href"]))
#    reposts = json.loads(urllib.request.urlopen(reposts["next_href"]+"&client_id=app.config["APY_KEY"]").read())

    
#   for item in list(reposts["collection"]):
#        #print ("item : " + str(item))
#        print("#################################################")
#        #if(item == 'track-repost'):
#        #for value in dict.items(item["track"]["id"]):
#        if(item["type"] == "track-repost") :
#            print("value : " + str(item["track"]["id"]))
#            #print ("key : " + str(key) +" - value : " + str(value))
