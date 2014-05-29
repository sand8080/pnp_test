import json
from pecan import expose

from sketch import plugin_handler


class ApiController(object):

    @expose()
    def index(self):
        return 'Api access point'

    @expose()
    @plugin_handler.api_hook('time')
    @plugin_handler.api_extension
    def add_node(self):
        res = {'status': 'ok', 'id': 77}
        return json.dumps(res)
