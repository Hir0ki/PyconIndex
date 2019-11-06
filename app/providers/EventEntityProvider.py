"""A EventEntity Service Provider."""

from masonite.provider import ServiceProvider
from app.entities.EventEntity import EventEntity

class EventEntityProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind('EventEntity', EventEntity)

    def boot(self):
        """Boots services required by the container."""
        pass
