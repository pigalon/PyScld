import soundcloud

def getPostedTracks(client, streamId, pgsize):
    return client.get('/users/'+streamId+'/tracks' , limit=pgsize, order='id',
                   linked_partitioning=1)

def getFavoriteTracks(client, streamId, pgsize):
    return client.get('/users/'+streamId+'/favorites' , limit=pgsize, order='id',
                   linked_partitioning=1)

def listAndPrintAllTracks(tracks):
    cpt=0

    for track in tracks.collection:
        cpt = cpt + 1
        print ("track n" + str(cpt) + " : " + track.title)
        

    try:
        while tracks.next_href != None:
            tracks = client.get(tracks.next_href , limit=pgsize, order='id',
                linked_partitioning=1)
            for track in tracks.collection:
                cpt = cpt + 1
                print ("track n" + str(cpt) + " : " + track.title)
    except AttributeError as e:
                print('End of the list: ' + str(e))


# get the client instance
client = soundcloud.Client(client_id=app.config["APY_KEY"])

# get the stream from one user
stream = client.get('/users/propellerrecordings')
print(stream.id)


pgsize=100
#tracks = client.get('/users/1158174/tracks' , limit=pgsize, order='id',
#                   linked_partitioning=1)

listAndPrintAllTracks(getPostedTracks(client, '31908119', pgsize))

listAndPrintAllTracks(getFavoriteTracks(client, '31908119', pgsize))

