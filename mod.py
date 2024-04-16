  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 1301, in render
    self.environment.handle_exception()
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 936, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 1, in top-level template code
    {% extends 'base.html' %}
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/base.html", line 10, in top-level template code
    {% block content %}{% endblock %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 58, in block 'content'
    <p class="product-portfolios"><strong>Portfolios:</strong> {{ ', '.join(portfolio_names) }}</p>
    ^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: sequence item 0: expected str instance, NoneType found
