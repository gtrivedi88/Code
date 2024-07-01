Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'app', an ImportError was raised:

Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 219, in locate_app
    __import__(module_name)
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 9, in <module>
    from routes.view_routes import view_routes
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 5, in <module>
    from app import cache
ImportError: cannot import name 'cache' from partially initialized module 'app' (most likely due to a circular import) (/home/gtrivedi/git/gitlab/opl-ui/app.py)
