import soundcloud

def getFollowers(client, streamId, pgsize):
    return client.get('/users/'+str(streamId)+'/followers' , limit=pgsize, order='id',
                   linked_partitioning=1)

def getFollowings(client, streamId, pgsize):
    return client.get('/users/'+str(streamId)+'/followings' , limit=pgsize, order='id',
                   linked_partitioning=1)

def listAndPrintAllUsers(users):
    cpt=0

    for user in users.collection:
        cpt = cpt + 1
        print ("user n" + str(cpt) + " : " + user.username + " - " + str(user.id))
        

    try:
        while users.next_href != None:
            users = client.get(users.next_href , limit=pgsize, order='id',
                linked_partitioning=1)
            for user in users.collection:
                cpt = cpt + 1
                print ("user n" + str(cpt) + " : " + user.username  + " - " + str(user.id))
    except AttributeError as e:
                print('End of the list: ' + str(e))


# get the client instance
client = soundcloud.Client(client_id=app.config["APY_KEY"]

# get the stream from one user
stream = client.get('/users/pierrock')
print(stream.id)

pgsize=100
#tracks = client.get('/users/1158174/tracks' , limit=pgsize, order='id',
#                   linked_partitioning=1)

listAndPrintAllUsers(getFollowings(client, stream.id, pgsize))

listAndPrintAllUsers(getFollowers(client, stream.id, pgsize))

