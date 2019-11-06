from app.models.Event import Event
from datetime import date
from orator.exceptions.query import QueryException
from wsgi import container
import json


class EventEntity:
    """ Entity class for Events """

    def __init__(self):
        self.event = container.make(Event)
    def create(
        self,
        name: str,
        youtube_url: str = None,
        website_url: str = None,
        start_date: date = None,
        end_date: date = None,
    ):
        """create instance of Event on databaes"""
        try:
            event = self.event.create(
                name=name,
                youtube_url=youtube_url,
                website_url=website_url,
                start_date=start_date,
                end_date=end_date,
            )
        except QueryException as error:
            raise ValueError(error)

        

    def get_all(self):
        """retunrs all instaces of event"""
        
        return self.event.all() 