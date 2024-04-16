  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 48, in view_products
    product['portfolio_names'] = [name for name in product['portfolio_names'] if name]
                                                   ~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "lib/sqlalchemy/cyextension/resultproxy.pyx", line 48, in sqlalchemy.cyextension.resultproxy.BaseRow.__getitem__
TypeError: tuple indices must be integers or slices, not str
