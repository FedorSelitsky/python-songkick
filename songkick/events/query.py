from .models import SongkickEvent
from ..query import SongkickQuery


class EventQuery(SongkickQuery):
    "Events-specific query backend"
    
    ResponseClass = SongkickEvent
    ResponseEnclosure = 'event'
    
    def get_api_path(self):
        "Generate the API resource path"

        if 'musicbrainz_id' in self._query:
            return 'artists/mbid:%s/events.json' % \
                   self._query.pop('musicbrainz_id')
        return 'events.json'
