"""A PyconAdminController Module."""

from masonite.request import Request
from masonite.response import Response
from masonite.view import View
from masonite.controllers import Controller
from masonite import app
from app.models.Event import Event
 

class PyconAdminController(Controller):
    """PyconAdminController Controller Class."""

    def __init__(self, request: Request):
        """PyconAdminController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('Event')

    def store(self, request: Request, event: Event):
        print(request.input("start-date"))
        event.create(
            name=request.input('event-name'),
            youtube_url=request.input('youtube_url'),
            website_url=request.input('website-url'),
            start_date=request.input('start-date'),
            end_date=request.input('end-date'),
        )
        return 'post created'