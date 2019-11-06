"""A PyconAdminController Module."""

from masonite.request import Request
from masonite.response import Response
from masonite.view import View
from masonite.controllers import Controller
from masonite import app
from app.entities.EventEntity import EventEntity
from datetime import date


class AdminEventController(Controller):
    """AdminEventController Controller Class."""

    def __init__(self, request: Request):
        """AdminEventController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, event: EventEntity):
        event = EventEntity()
        return view.render("Event", {"events": event.get_all()})

    def store(self, request: Request, response: Response, event: EventEntity):
        event = EventEntity()
        try:
            start_date = date.fromisoformat(request.input("start_date"))
        except ValueError:
            start_date = None
        try:
            end_date = date.fromisoformat(request.input("end_date"))
        except ValueError:
            end_date = None

        event.create(
            name=request.input("event_name"),
            youtube_url=request.input("youtube_url"),
            website_url=request.input("website_url"),
            start_date=start_date,
            end_date=end_date,
        )

        return response.redirect("/admin/event")

