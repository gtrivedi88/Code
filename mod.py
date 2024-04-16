  File "/usr/lib/python3.12/site-packages/jinja2/loaders.py", line 137, in load
    code = environment.compile(source, name, filename)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 768, in compile
    self.handle_exception(source=source_hint)
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 936, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 58, in template
    <p class="product-portfolios"><strong>Portfolios:</strong> {{ ', '.join([name for name in
    ^^^^^^^^^^^^^^^^^^^^^^^^^
jinja2.exceptions.TemplateSyntaxError: expected token ',', got 'for'
