127.0.0.1 - - [31/May/2024 21:23:23] "GET /static/scripts/product_type.js HTTP/1.1" 200 -
SELECT brand_opl.product.product_id AS brand_opl_product_product_id, brand_opl.product.product_name AS brand_opl_product_product_name, brand_opl.product.product_status AS brand_opl_product_product_status, brand_opl.product.last_updated AS brand_opl_product_last_updated, coalesce(array_agg(DISTINCT brand_opl.product_portfolios.category_name) FILTER (WHERE brand_opl.product_portfolios.category_name IS NOT NULL)) AS portfolio_names, array_agg(DISTINCT brand_opl.product_types.product_type) AS product_types 
FROM brand_opl.product LEFT OUTER JOIN brand_opl.product_portfolio_map ON brand_opl.product.product_id = brand_opl.product_portfolio_map.product_id LEFT OUTER JOIN brand_opl.product_portfolios ON brand_opl.product_portfolio_map.category_id = brand_opl.product_portfolios.category_id JOIN brand_opl.product_types_map ON brand_opl.product_types_map.product_id = brand_opl.product.product_id JOIN brand_opl.product_types ON brand_opl.product_types.type_id = brand_opl.product_types_map.type_id LEFT OUTER JOIN brand_opl.product_alias ON brand_opl.product_alias.product_id = brand_opl.product.product_id GROUP BY brand_opl.product.product_id, brand_opl.product.product_name, brand_opl.product.product_status, brand_opl.product.last_updated ORDER BY brand_opl.product.product_name
[2024-05-31 21:23:25,972] ERROR in app: Exception on /opl/search-to-view-products [GET]
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
  File "/home/gtrivedi/git/gitlab/opl-ui/routes/view_routes.py", line 54, in view_products
    print(products_with_portfolios)
          ^^^^^^^^^^^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'products_with_portfolios' where it is not associated with a value









@view_routes.route('/opl/search-to-view-products', methods=['GET', 'POST'])
def view_products():
    # Initialize the search form
    form = SearchForm()

    # Define the base query for products, including the portfolio name
    products_query = db.session.query(
        Product.product_id,
        Product.product_name,
        Product.product_status,
        Product.last_updated,
        func.coalesce(func.array_agg(distinct(ProductPortfolios.category_name)).filter(ProductPortfolios.category_name != None)).label('portfolio_names'),
        func.array_agg(distinct(ProductType.product_type)).label('product_types')
    ).outerjoin(ProductPortfolioMap, Product.product_id == ProductPortfolioMap.product_id) \
      .outerjoin(ProductPortfolios, ProductPortfolioMap.category_id == ProductPortfolios.category_id) \
      .join(ProductTypeMap, ProductTypeMap.product_id == Product.product_id) \
      .join(ProductType, ProductType.type_id == ProductTypeMap.type_id) \
      .outerjoin(ProductAlias, ProductAlias.product_id == Product.product_id) \
      .group_by(Product.product_id, Product.product_name, Product.product_status, Product.last_updated) \
      .order_by(Product.product_name)

    if form.validate_on_submit():
        if form.product_name.data:
            search_term = f"%{form.product_name.data}%"
            products_query = products_query.filter(
                or_(
                    Product.product_name.ilike(search_term),
                    ProductAlias.alias_name.ilike(search_term)
                )
            )
        if form.product_status.data and form.product_status.data != 'Select':
            products_query = products_query.filter(Product.product_status == form.product_status.data)
        if form.product_type.data and form.product_type.data:
            type_id = form.product_type.data
            if isinstance(type_id, list):
                type_id = type_id[0]
            products_query = products_query.filter(ProductType.type_id == type_id)

    # Get the list of products based on the filtered and now sorted query
    print(products_query)
    products = products_query.all()

    print(products_with_portfolios)
    products_with_portfolios = products_query.all()


    # Convert each tuple to a dictionary for easier access
    products_with_portfolios = [
        {
            'product_id': product[0],
            'product_name': product[1],
            'product_status': product[2],
            'last_updated': product[3],
            'portfolio_names': product[4],
            'product_types': product[5]
        }
        for product in products_with_portfolios
    ]

    # Preprocess portfolio names to filter out None values
    for product in products_with_portfolios:
        product['portfolio_names'] = [name for name in product['portfolio_names'] if name]

    # Check if a specific product is selected to display detailed information
    selected_product_id = request.args.get('product_id')
    selected_product = Product.query.get(selected_product_id) if selected_product_id else None

    return render_template('opl/view_search.html', form=form, products=products, selected_product=selected_product, products_with_portfolios=products_with_portfolios)



{% if form.is_submitted() and form.validate() %}
<fieldset class="pf-v5-c-form">
    <legend class="pf-v5-c-title">Search results</legend>
    <div class="pf-v5-c-content">
        {% if products_with_portfolios %}
        <ul class="pf-v5-c-list">
            {% for product in products_with_portfolios %}
            <li class="pf-v5-c-list__item">
                <div class="pf-v5-c-content">
                    <p class="pf-v5-c-title">
                        <a href="{{ url_for('view_routes.view_product_details', product_id=product.product_id) }}">
                            {{ product.product_name }}
                        </a>
                    </p>
                    <p><strong>Status:</strong> {{ product.product_status }}</p>
                    <p><strong>Last Updated:</strong> {{ product.last_updated.strftime('%d %B %Y') }}</p>
                    {% if product.portfolio_names and product.portfolio_names|select('!=', None)|list|length > 0 %}
                    <p><strong>Portfolios:</strong> {{ product.portfolio_names|join(', ') }}</p>
                    {% endif %}
                    <p><strong>Product Types:</strong> {{ ', '.join(product.product_types) }}</p>
                </div>
            </li>
            {% endfor %}
        </ul>
        {% else %}
        <p>No results found.</p>
        {% endif %}
    </div>
</fieldset>
{% endif %}
</div>
{% endblock %}
