from arango_orm import Database, Collection, Relation, Graph, GraphConnection
from arango_orm.fields import List, String, UUID, Integer, Boolean, DateTime, Date


from util.BaseUtil import StringUtil
from util.BaseUtil import DateUtil


class User(Collection):

    __collection__ = 'Users'

    _key = String(required=True)
    username = String(required=True, allow_none=False)
    full_name = String()

    repost_count = Integer()
    track_count = Integer()
    playlist_count = Integer()
    followers_count = Integer()
    followings_count = Integer()
    public_favorites_count = Integer()

    permalink = String()
    uri = String()
    permalink_url = String()
    avatar_url = String()
    degree = Integer()
    dt_bd_action = DateTime()



    def convert(self, soundcloudUser):
        print("souncloudUser : " + str(soundcloudUser))
        self._key = soundcloudUser.id
        self.username = soundcloudUser.username
        self.full_name = soundcloudUser.full_name

        self.track_count = soundcloudUser.track_count
        self.playlist_count = soundcloudUser.playlist_count
        self.followers_count = soundcloudUser.followers_count
        self.followings_count = soundcloudUser.followings_count
        self.public_favorites_count = soundcloudUser.public_favorites_count

        self.permalink = soundcloudUser.permalink
        self.uri = soundcloudUser.uri
        self.permalink_url = soundcloudUser.permalink_url
        self.avatar_url = soundcloudUser.avatar_url
    
    def display(self):
        print(self.__dict__)
    
    def change_degree(self, degree):
        self.degree=degree

    def delta_playlist_count(self, user):
        return user.playlist_count - self.playlist_count

    def delta_public_favorites_count(self, user):
        return user.public_favorites_count - self.public_favorites_count

    def delta_track_count (self, user):
        return user.track_count - self.track_count

    def delta_repost_count (self, user):
        return user.repost_count - self.repost_count

    def delta_followers_count (self, user):
        return user.followers_count - self.followers_count

    def delta_followings_count (self, user):
        return user.followings_count - self.followings_count

    def to_dict(self):
        return {
            '_key': self._key,
            'username': self.username,
            'full_name': self.full_name,
            'degree': self.degree,
            'track_count': self.track_count,
            'playlist_count':self.playlist_count,
            'followers_count':self.followers_count,
            'followings_count':self.followings_count,
            'public_favorites_count':self.public_favorites_count,
            'permalink':self.permalink,
            'uri':self.uri,
            'avatar_url':self.avatar_url
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    



