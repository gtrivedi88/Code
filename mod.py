Press CTRL+C to quit
[2024-06-29 00:53:16,316] ERROR in app: Exception on /opl/edit-product/a14b0aaa-00d9-4e37-bdad-0c145afdc0b4 [GET]
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
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_principal.py", line 199, in _decorated
    rv = f(*args, **kw)
         ^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/edit_routes.py", line 113, in edit_product_details
    reference_form = ReferenceForm()
                     ^^^^^^^^^^^^^
NameError: name 'ReferenceForm' is not defined. Did you mean: 'ReferenceError'?
