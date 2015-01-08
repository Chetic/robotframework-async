Generic Robot Framework library for asynchronous keyword execution

Installation
============
If you have pip installed:
``pip install robotframework-async``

Alternatively download directly from the Python Package Index: https://pypi.python.org/pypi/robotframework-async

Usage
=====
#) Import into a test suite with:
    ``Library AsyncLibrary``

#) To run a keyword asynchronously:
    ``${handle}    async run    some keyword    first argument    second argument``

#) To retrieve the return value, a blocking call to async_get is called with the handle:
    ``${return_value}    async get    ${handle}``
