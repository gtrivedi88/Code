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
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.SyntaxError) syntax error at or near "DISTINCT"
LINE 1: ...ame), ARRAY['No Portfolios']) AS portfolio_names, DISTINCT a...
                                                             ^

[SQL: SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, coalesce(array_agg(brand_opl.product_portfolios.category_name), %(coalesce_1)s) AS portfolio_names, DISTINCT array_agg(brand_opl.product_types.product_type) AS product_types 
FROM brand_opl.product LEFT OUTER JOIN brand_opl.product_portfolio_map ON brand_opl.product.product_id = brand_opl.product_portfolio_map.product_id LEFT OUTER JOIN brand_opl.product_portfolios ON brand_opl.product_portfolio_map.category_id = brand_opl.product_portfolios.category_id JOIN brand_opl.product_types_map ON brand_opl.product_types_map.product_id = brand_opl.product.product_id JOIN brand_opl.product_types ON brand_opl.product_types_map.type_id = brand_opl.product_types.type_id GROUP BY brand_opl.product.product_id, brand_opl.product.product_name, brand_opl.product.product_status, brand_opl.product.last_updated ORDER BY brand_opl.product.product_name]
[parameters: {'coalesce_1': ['No Portfolios']}]
(Background on this error at: https://sqlalche.me/e/20/f405)
