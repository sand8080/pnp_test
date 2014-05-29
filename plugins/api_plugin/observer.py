import datetime
from sketch.plugin import ApiPlugin


class ExecutionTime(ApiPlugin):

    def __init__(self):
        self.start = None

    def __call__(self, *args, **kwargs):
        return "### Execution time. __call__()"

    def pre(self, *args, **kwargs):
        self.start = datetime.datetime.now()
        return "### Execution time. pre called"

    def post(self, *args, **kwargs):
        return "### Execution time. post called. result: {0}".format(
            datetime.datetime.now() - self.start
        )
