from arango_orm import Database

from ardb.Track import Track

class TrackRepo():

    def __init__(self, db):
        self.db = db
        
    def read_from_db(self, trackId):
        return trackId

    def sc_to_db(self, track, ranking):
        t= Track()
        t.convert(soundcloudTrack=track)
        t.ranking = ranking
        try :
            self.db.add(t)
            print('added : ')
            return True
        except Exception as e:
            print('Already stored! : ' + str(e))
            return False

    def write(self, track, ranking):
        track.ranking = ranking
        try :
            self.db.add(track)
            print('added : ')
            return True
        except Exception as e:
            print('Already stored! : '+e.__class__.__name__)
            return False

    def write_list(self, allTracks, ranking):
        cpt = 0
        cpt_added = 0
        cpt_canceled = 0
        for track in allTracks :
            cpt = cpt + 1
            print(str(cpt) + " add track : " + str(track._key) + " - " + track.title)
            if (self.write(track=track, ranking=ranking)) : 
                cpt_added = cpt_added + 1
                print("added cpt : " + str(cpt_added))
            else :
                cpt_canceled = cpt_canceled + 1
                print("canceled cpt : " + str(cpt_canceled))



        
