"""Testevent Testcase."""
from masonite.testing import TestCase
from config.factories import factory
from app.Entities.EventEntity import EventEntity
from app.models.Event import Event
from masonite import Cache
from wsgi import container


class TestEventSelection(TestCase):

    """All tests by default will run inside of a database transaction."""

    transactions = True

    def setUp(self):
        """Anytime you override the setUp method you must call the setUp method
        on the parent class like below.
        """
        super().setUp()

    def setUpFactories(self):
        """This runs when the test class first starts up.
        This does not run before every test case. Use this method to
        set your database up.
        """
        #        factory(Event, 8).create()
        # self.make(Event, self.events_factory, 8)
        from faker import Faker

        faker = Faker()
        event = EventEntity(Event())
        self.youtube_url = 'https://youtube.com'
        for n in range(0, 8):
            event.create(
                name=faker.name(),
                youtube_url=self.youtube_url,
                website_url=faker.url(),
                start_date=faker.date(),
                end_date=faker.date(),
            )


    def test_get_all(self):
        cache = container.make(Cache)
        eventEntity = EventEntity(Event())
        events = eventEntity.get_all()
        for event in events:
            if event.youtube_url != self.youtube_url:
                self.fail("Didn't retreve the rigth date back from cache")
        self.assertEqual(len(events), 8)
        cache.delete("all_events")

