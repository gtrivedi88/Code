  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/selectable.py", line 1323, in _match_primaries
    return self._join_condition(left, right, a_subset=left_right)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/selectable.py", line 1346, in _join_condition
    cls._joincond_trim_constraints(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/selectable.py", line 1491, in _joincond_trim_constraints
    raise exc.AmbiguousForeignKeysError(
sqlalchemy.exc.AmbiguousForeignKeysError: Can't determine join between 'Join object on Join object on Join object on Join object on Join object on product(139668729333664) and product_portfolio_map(139668729191872)(139668727399344) and product_portfolios(139668729192112)(139668727399920) and product_types_map(139668729192208)(139668727400112) and product_types(139668740978016)(139668727400064) and product_alias(139668729194080)' and 'product_types_map'; tables have more than one foreign key constraint relationship between them. Please specify the 'onclause' of this join explicitly.
