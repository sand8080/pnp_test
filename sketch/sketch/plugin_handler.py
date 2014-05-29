import functools
import json
from threading import RLock
from stevedore import ExtensionManager

from stevedore.hook import HookManager
from stevedore.driver import DriverManager


objs_cache = {}
objs_cache_lock = RLock()


# def driver(interface, name, *dt, **mp):
#     key = (interface, name)
#
#     with objs_cache_lock:
#         if key in objs_cache:
#             return objs_cache[key]
#
#     pcls = DriverManager(interface.namespace, name)
#
#     with objs_cache_lock:
#         if key in objs_cache:
#             return objs_cache[key]
#         else:
#             obj = pcls(*dt, **mp)
#             objs_cache[key] = obj
#
#     return obj


def api_hook(name):
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            print "### in api_hook"
            key = name
            namespace = 'api_call.observer'

            print "### key, namespase", key, namespace
            with objs_cache_lock:
                manager = objs_cache.setdefault(key, HookManager(namespace, name, invoke_on_load=True))

            print "### manager", manager
            print "### discovered extensions", manager.names()
            plugin_result = []

            def handle_pre_api_call(ext):
                return ext.name, ext.obj.pre(*args, **kwargs)

            if manager.extensions:
                plugin_result += manager.map(handle_pre_api_call)

            result = func(*args, **kwargs)
            plugin_result.append(result)

            def handle_post_api_call(ext):
                return ext.name, ext.obj.post(*args, **kwargs)

            if manager.extensions:
                plugin_result += manager.map(handle_post_api_call)

            print "### plugin_result", plugin_result
            return json.dumps(plugin_result)
            return result
        return decorated
    return decorator

