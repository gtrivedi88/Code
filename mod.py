INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on https://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
ERROR:app:Exception on /opl/search-to-view-products [GET]
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_caching/__init__.py", line 392, in decorated_function
    rv = self.cache.get(cache_key)
         ^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_caching/__init__.py", line 191, in cache
    return app.extensions["cache"][self]
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
KeyError: <flask_caching.Cache object at 0x7f17d7965c70>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_caching/__init__.py", line 410, in decorated_function
    if self.app.debug:
       ^^^^^^^^
AttributeError: 'Cache' object has no attribute 'app'
