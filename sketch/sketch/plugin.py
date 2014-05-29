import abc


class ApiPlugin(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def pre(self):
        pass

    @abc.abstractmethod
    def post(self):
        pass


# if __name__ == '__main__':
#     a = ApiPlugin()
#     print "ok"