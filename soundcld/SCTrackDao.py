
class SCTrackDao():

    # Constructor
    def __init__(self, clientSC):
        self.clientSC = clientSC
    
    # get user sc obj
    def get(self, param):
        try :
            return self.clientSC.get('/tracks/'+str(param))
        except Exception as e:
            print("Exception get tracks from SC : " + param +" - e:" +e)
            return None
