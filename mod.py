  File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/view_search.html", line 58, in block 'content'
    <p class="product-portfolio"><strong>Portfolio:</strong> {{ product.ProductPortfolios.category_name }}</p>
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/jinja2/environment.py", line 485, in getattr
    return getattr(obj, attribute)
           ^^^^^^^^^^^^^^^^^^^^^^^
jinja2.exceptions.UndefinedError: 'sqlalchemy.engine.row.Row object' has no attribute 'ProductPortfolios'
