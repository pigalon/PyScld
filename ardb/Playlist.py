
from arango import ArangoClient
from arango_orm import Database, Collection, Relation, Graph, GraphConnection
from arango_orm.fields import List, String, UUID, Integer, Boolean, DateTime, Date

from util.BaseUtil import StringUtil
from util.BaseUtil import DateUtil


class Playlist(Collection):

    __collection__ = 'Playlists'

    _key = String(required=True)
    title = String(required=True, allow_none=False)
    user_id = String()
    track_count = Integer()
    created_at = DateTime()
    ranking = Integer()
    duration = Integer()
    genre = String(allow_none=True)
    permalink = String()
    description = String(allow_none=True)
    uri = String()
    label_name = String(allow_none=True)
    tags_list = List(String())
    tags_family = List(String())
    last_modified = DateTime()
    artwork_url = String(allow_none=True)
    dynamic = Integer()
    img = String()
    folder = String()
    tracks = List(String())

    def convert(self, soundcloudPlaylist):
        self._key = soundcloudPlaylist.id
        self.title = soundcloudPlaylist.title
        self.user_id = str(soundcloudPlaylist.user_id)
        self.track_count = soundcloudPlaylist.track_count
        self.created_at = DateUtil.dateStr_to_datetime(soundcloudPlaylist.created_at)
        self.last_modified = DateUtil.dateStr_to_datetime(soundcloudPlaylist.last_modified)
        self.ranking=0
        list = []
        list = StringUtil.tagsStr_to_list(tagsStr=soundcloudPlaylist.tag_list)
        print ("::::: " + str(list))
        self.tags_list =  list#
        self.genre = soundcloudPlaylist.genre
        self.tags_family = ["pierrick"]
        self.duration = soundcloudPlaylist.duration
        self.permalink = soundcloudPlaylist.permalink
        self.description = soundcloudPlaylist.description
        self.label_name = soundcloudPlaylist.label_name
        self.uri = soundcloudPlaylist.uri
        self.permalink_url = soundcloudPlaylist.permalink_url
        self.artwork_url = soundcloudPlaylist.artwork_url
        self.dynamic = 0
        self.img = ""
        self.folder = ""
        list = []
        for track in soundcloudPlaylist.tracks :
            #print("track : " + str(track))
            list.append(str(track["id"])) 
        self.tracks = list
    
    def display(self):
        print(self.__dict__)

    def to_dict(self):
        return {
            '_key': self._key,
            'title': self.title,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'track_count': self.track_count,
            'ranking':self.ranking,
            'duration':self.duration,
            'genre':self.genre,
            'permalink':self.permalink,
            'description':self.description,
            'uri':self.uri,
            'label_name':self.label_name,
            'tags_list':self.tags_list,
            'tags_family':self.tags_family,
            'last_modified':self.last_modified,
            'artwork_url':self.artwork_url,
            'dynamic':self.dynamic,
            'img':self.img,
            'folder':self.folder,
            'tracks':self.tracks
        }
    

