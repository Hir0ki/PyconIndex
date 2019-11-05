"""A PyconAdminController Module."""

from masonite.request import Request
from masonite.response import Response
from masonite.view import View
from masonite.controllers import Controller
from masonite import app
from app.models.Event import Event
from datetime import date

class AdminEventController(Controller):
    """AdminEventController Controller Class."""

    def __init__(self, request: Request):
        """AdminEventController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, event: Event):
        return view.render('Event')

    def store(self, request: Request, event: Event, response: Response):
        try:
            start_date=date.fromisoformat(request.input('start_date'))
        except ValueError:
            start_date = None
        try:
            end_date=date.fromisoformat(request.input('end_date'))
        except ValueError:
            end_date = None

        

        return response.redirect('/admin/event')