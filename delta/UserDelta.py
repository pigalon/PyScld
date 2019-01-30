from arangodb import User
class UserDelta():

    track_delta = 0
    playlist_delta = 0
    followers_delta = 0
    followings_delta = 0
    public_favorites_delta = 0

    id_user_db="0"
    id_user_sc="0"

    # Constructor
    def __init__(self, userDB, userNet):
        self.id_user_db = userDB._key
        self.id_user_sc = userNet._key

        self.playlist_delta = userDB.delta_playlist_count(userNet)
        self.track_delta = userDB.delta_track_count(userNet)
        self.public_favorites_count = userDB.delta_public_favorites_count (userNet)
        self.followers_delta=userDB=userDB.delta_followers_count(userNet)
        self.followings_delta=userDB.userDB.delta_followings_count(userNet)
