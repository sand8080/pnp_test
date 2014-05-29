from sketch.plugin import ApiPlugin


class ExecutionTime(ApiPlugin):

    def __call__(self, *args, **kwargs):
        result = "### Execution time. __call__()"
        print result
        return result

    def pre(self, *args, **kwargs):
        result = "### Execution time. pre called"
        print result
        return result

    def post(self, *args, **kwargs):
        result = "### Execution time. post called"
        print result
        return result


# if __name__ == '__main__':
#     e = ExecutionTime()
#     print "### ", e.namespace
#     print "ok"