Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedFunction: function listagg(character varying, unknown, character varying) does not exist
LINE 1: ...dated AS brand_opl_product_last_updated, coalesce(listagg(CA...
                                                             ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.


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
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 61, in view_products
    products = products_query.all()
               ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/query.py", line 2693, in all
    return self._iter().all()  # type: ignore
           ^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/query.py", line 2847, in _iter
    result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
                                                  ^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 2308, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 2190, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
    return meth(
           ^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2343, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedFunction) function listagg(character varying, unknown, character varying) does not exist
LINE 1: ...dated AS brand_opl_product_last_updated, coalesce(listagg(CA...
                                                             ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.

[SQL: SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, coalesce(listagg(CASE WHEN (brand_opl.product_portfolios.category_name IS NOT NULL) THEN brand_opl.product_portfolios.category_name END, %(listagg_1)s) WITHIN GROUP (ORDER BY brand_opl.product_portfolios.category_name), %(coalesce_1)s) AS portfolio_names, listagg(brand_opl.product_types.product_type, %(listagg_2)s) WITHIN GROUP (ORDER BY brand_opl.product_types.product_type) AS product_types 
FROM brand_opl.product LEFT OUTER JOIN brand_opl.product_portfolio_map ON brand_opl.product.product_id = brand_opl.product_portfolio_map.product_id LEFT OUTER JOIN brand_opl.product_portfolios ON brand_opl.product_portfolio_map.category_id = brand_opl.product_portfolios.category_id JOIN brand_opl.product_types_map ON brand_opl.product_types_map.product_id = brand_opl.product.product_id JOIN brand_opl.product_types ON brand_opl.product_types.type_id = brand_opl.product_types_map.type_id LEFT OUTER JOIN brand_opl.product_alias ON brand_opl.product_alias.product_id = brand_opl.product.product_id GROUP BY brand_opl.product.product_id, brand_opl.product.product_name, brand_opl.product.product_status, brand_opl.product.last_updated ORDER BY brand_opl.product.product_name]
[parameters: {'listagg_1': ', ', 'coalesce_1': '', 'listagg_2': ', '}]
(Background on this error at: https://sqlalche.me/e/20/f405)
