from sketch.controllers.api import ApiController
from pecan import expose


class RootController(object):

    @expose()
    def index(self):
        return 'Index'

    api = ApiController()