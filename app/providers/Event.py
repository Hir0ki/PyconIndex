"""A Event Service Provider."""

from masonite.provider import ServiceProvider
from app.models.Event import Event

class Event(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind('Event', Event)

    def boot(self):
        """Boots services required by the container."""
        pass
