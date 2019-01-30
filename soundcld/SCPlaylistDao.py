from arangodb.Track import Track
from arangodb.Playlist import Playlist


class SCPlaylistDao():

    # Constructor
    def __init__(self, clientSC):
        self.clientSC = clientSC
    
    # get playlist sc obj
    def get(self, param):
        try :
            return self.clientSC.get('/playlists/'+str(param))
        except Exception as e:
            print("Exception get tracks from SC : " + param +" - e:" +e)
            return None
    
    def getAllConvertedPlaylist(self, playlists) :
        convertedPlaylists = []
        for playlist in playlists :
            p = Playlist()
            p.convert(soundcloudPlaylist=playlist)
            convertedPlaylists.append(p)
        return convertedPlaylists
    
    def getAllConvertedTracks(self, playlist):
        tracks = []
        for track in playlist.tracks :
            print("track : " + str(track["id"]) + " - " + track["title"])
            t= Track()
            t.convert_from_json_playlis(soundcloudTrack=track)
            tracks.append(t)
        return tracks

        