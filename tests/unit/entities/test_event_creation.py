"""Testevent_creation Testcase."""

from masonite.testing import TestCase
from app.entities.EventEntity import EventEntity
from datetime import date, timedelta
from app.models.Event import Event

class Testevent_creation(TestCase):

    """All tests by default will run inside of a database transaction."""
    transactions = True

    def setUp(self):
        """Anytime you override the setUp method you must call the setUp method
        on the parent class like below.
        """
        super().setUp()
        self.eventEntity = EventEntity()

    def setUpFactories(self):
        """This runs when the test class first starts up.
        This does not run before every test case. Use this method to
        set your database up.
        """
        pass

    
    def test_create_event_new(self):
        name = "Pycon2017"
        youtube_url="https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ"
        self.eventEntity.create(
            name=name,
            youtube_url=youtube_url,
            website_url="https://pycon.blogspot.com/",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1), 
        )

        event = Event.where('name', '=', name).get()

        self.assertEqual(event[0].youtube_url , youtube_url)


    def test_create_event_double(self):
        name = "Pycon2019"
        youtube_url="https://www.youtube.com/channel/test01"
        website_url= "https://pycon.blogspot.com/"
        try:
            self.eventEntity.create(
                name=name,
                youtube_url=youtube_url,
                website_url=website_url,
                start_date=date.today(),
                end_date=date.today() + timedelta(days=1), 
            )
        except ValueError:
            self.fail("Should create the first instance of EventEvntity")
        raised_exception = False
        try:
            self.eventEntity.create(
                name=name,
                youtube_url=youtube_url,
                website_url=website_url,
                start_date=date.today(),
                end_date=date.today() + timedelta(days=1), 
            )
        except ValueError:
            self.assertTrue(True)
            raised_exception = True

        if raised_exception == False:
            self.fail("No exception was raised after double assignement")
        
