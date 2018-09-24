import sys
import os
import time
from robot.libraries.BuiltIn import BuiltIn
from robot.output import librarylogger as log
from robot.running import Keyword
from robot.running.context import EXECUTION_CONTEXTS

class AsyncLibrary:
    def __init__(self):
        self._thread_pool = {}
        self._last_thread_handle = 0

    def async_run(self, keyword, *args, **kwargs):
        ''' Executes the provided Robot Framework keyword in a separate thread and immediately returns a handle to be used with async_get '''
        handle = self._last_thread_handle
        thread = self._threaded(keyword, *args, **kwargs)
        thread.start()
        self._thread_pool[handle] = thread
        self._last_thread_handle += 1
        return handle

    def async_get(self, handle):
        ''' Blocks until the thread created by async_run returns '''
        assert handle in self._thread_pool, 'Invalid async call handle'
        result = self._thread_pool[handle].result_queue.get()
        del self._thread_pool[handle]
        return result

    def _get_handler_from_keyword(self, keyword):
        ''' Gets the Robot Framework handler associated with the given keyword '''
        if EXECUTION_CONTEXTS.current is None:
            raise RobotNotRunningError('Cannot access execution context')
        return EXECUTION_CONTEXTS.current.get_handler(keyword)

    def _threaded(self, keyword, *args, **kwargs):
        try:
            import queue
        except ImportError:
            import Queue as queue
        import threading
        
        def wrapped_f(q, *args, **kwargs):
            ''' Calls the decorated function and puts the result in a queue '''
            f = self._get_handler_from_keyword(keyword)
            ret = f.run(EXECUTION_CONTEXTS.current, args)
            q.put(ret)

        q = queue.Queue()
        t = threading.Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        t.result_queue = q
        return t
