
from arango import ArangoClient
from arango_orm import Database, Collection, Relation, Graph, GraphConnection
from arango_orm.fields import List, String, UUID, Integer, Boolean, DateTime, Date

from soundcld.util.Util import StringUtil
from soundcld.util.Util import DateUtil



class Track(Collection):

    __collection__ = 'Tracks'

    _key = String(required=True)
    title = String(required=True)
    created_at = DateTime()
    ranking = Integer()
    tags_genre = List(String())
    tags_family = List(String())
    duration = Integer()
    permalink = String()
    description = String()
    label_name = String()
    release_year = String()
    release_month =  Integer() 
    release_day = Integer() 
    original_format =  String() 
    uri = String()
    permalink_url = String() 
    artwork_url = String()
    dynamic = Integer()
    img = String()
    mp3 = String()
    dt_bd_action = DateTime()


    def convert(self, soundcloudTrack):
        self._key = soundcloudTrack.id
        self.title = soundcloudTrack.title
        self.created_at = DateUtil.dateStr_to_datetime(soundcloudTrack.created_at)
        self.ranking=0
        list = []
        list = StringUtil.tagsStr_to_list(tagsStr=soundcloudTrack.tag_list)
        self.tags_genre =  list#
        self.tags_family = ["pierrick"]
        self.duration = soundcloudTrack.duration
        self.permalink = soundcloudTrack.permalink
        self.description = soundcloudTrack.description
        self.label_name = soundcloudTrack.label_name
        self.release_year = soundcloudTrack.release_year
        self.release_month =  soundcloudTrack.release_month
        self.release_day = soundcloudTrack.release_day
        self.original_format =  soundcloudTrack.original_format
        self.uri = soundcloudTrack.uri
        self.permalink_url = soundcloudTrack.permalink_url
        self.artwork_url = soundcloudTrack.artwork_url
        self.dynamic = 0
        self.img = ""
        self.mp3 = ""
        
    def convert_from_json(self, soundcloudTrack):
        self._key = soundcloudTrack["id"]
        self.title = soundcloudTrack["title"]
        self.created_at = DateUtil.dateJson_to_datetime(soundcloudTrack["created_at"])
        self.ranking=0
        list = []
        list = StringUtil.tagsStr_to_list(tagsStr=soundcloudTrack["tag_list"])
        self.tags_genre =  list#
        self.tags_family = ["pierrick"]
        self.duration = soundcloudTrack["duration"]
        self.permalink = soundcloudTrack["permalink"]
        self.description = soundcloudTrack["description"]
        self.label_name = soundcloudTrack["label_name"]
        #self.release_year = soundcloudTrack["release_year"]
        #self.release_month =  soundcloudTrack["release_month"]
        #self.release_day = soundcloudTrack["release_day"]
        #self.original_format =  soundcloudTrack["original_format"]
        self.uri = soundcloudTrack["uri"]
        self.permalink_url = soundcloudTrack["permalink_url"]
        self.artwork_url = soundcloudTrack["artwork_url"]
        self.dynamic = 0
        self.img = ""
        self.mp3 = ""

    def convert_from_json_playlis(self, soundcloudTrack):
        self._key = soundcloudTrack["id"]
        self.title = soundcloudTrack["title"]
        self.created_at = DateUtil.dateStr_to_datetime(soundcloudTrack["created_at"])
        self.ranking=0
        list = []
        list = StringUtil.tagsStr_to_list(tagsStr=soundcloudTrack["tag_list"])
        self.tags_genre =  list#
        self.tags_family = ["pierrick"]
        self.duration = soundcloudTrack["duration"]
        self.permalink = soundcloudTrack["permalink"]
        self.description = soundcloudTrack["description"]
        self.label_name = soundcloudTrack["label_name"]
        self.release_year = soundcloudTrack["release_year"]
        self.release_month =  soundcloudTrack["release_month"]
        self.release_day = soundcloudTrack["release_day"]
        self.original_format =  soundcloudTrack["original_format"]
        self.uri = soundcloudTrack["uri"]
        self.permalink_url = soundcloudTrack["permalink_url"]
        self.artwork_url = soundcloudTrack["artwork_url"]
        self.dynamic = 0
        self.img = ""
        self.mp3 = ""


