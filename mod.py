  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 47, in view_products
    return render_template('opl/view_search.html', form=form, products=products, selected_product=selected_product, products_with_portfolios=products_with_portfolios)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/templating.py", line 152, in render_template
    return _render(app, template, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/templating.py", line 133, in _render
    rv = template.render(context)
         ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 1301, in render
    self.environment.handle_exception()
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 936, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 1, in top-level template code
    {% extends 'base.html' %}
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/base.html", line 10, in top-level template code
    {% block content %}{% endblock %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 48, in block 'content'
    {% for product, portfolio in products_with_portfolios %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 2)
