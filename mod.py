[2024-06-06 13:31:03,955] ERROR in app: Exception on /opl/search-to-view-products [GET]
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/elements.py", line 1599, in __getattr__
    return getattr(self.comparator, key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Comparator' object has no attribute 'filter'

The above exception was the direct cause of the following exception:

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
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 22, in view_products
    func.coalesce(func.listagg(ProductPortfolios.category_name, ', ').within_group(ProductPortfolios.category_name).filter(ProductPortfolios.category_name != None), '').label('portfolio_names'),
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/elements.py", line 1601, in __getattr__
    raise AttributeError(
AttributeError: Neither 'WithinGroup' object nor 'Comparator' object has an attribute 'filter'
