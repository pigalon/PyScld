from arango_orm import Database

from ardb.Playlist import Playlist

class PlaylistRepo():

    def __init__(self, db):
        self.db = db
        
    def read_from_db(self, playlistId):
        return playlistId
    
    def get_list_by_user_id(self, user_id):
        print("user_id : " + str(user_id))
        list = self.db.query(Playlist).filter("user_id==@user_id", user_id=str(user_id)).all()
        print("tttt : " + str(len(list)))
        return list

    def sc_to_db(self, playlist, ranking):
        p= Playlist()
        p.convert(soundcloudPlaylist=playlist)
        p.ranking = ranking
        try :
            self.db.add(p)
            print('added : ')
            return True
        except Exception as e:
            print('Already stored! : ' + str(e))
            return False

    def write(self, playlist, ranking):
        playlist.ranking = ranking
        try :
            self.db.add(playlist)
            print('added : ')
            return True
        except Exception as e:
            print('Already stored! : '+e.__class__.__name__)
            return False

    def writeList(self, playlists, ranking):
        for playlist in playlists :
            self.write(playlist, ranking)
            


        
