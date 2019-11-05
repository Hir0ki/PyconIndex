from orator.orm import Factory
from app.models.User import User
from app.models.Event import Event

factory = Factory()


def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
    }


factory.register(User, users_factory)

        
def events_factory(faker):
    return {
        'name': faker.name(),
        'youtube_url': faker.url(),
        'website_url': faker.url(),
        'start_date': faker.date(),
        'end_date': faker.date(),
    }

factory.register(Event, events_factory)