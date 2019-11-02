from config.database import Model 

class Event(Model):
    """Model for all pycon events"""

    __table__ = 'Event'

    __fillable__ = ['name', 'youtube_url', 'website_url', 'start_date', 'end_date']