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
        func.coalesce(func.array_agg(distinct(ProductPortfolios.category_name)).filter(ProductPortfolios.category_name !=   None), []).label('portfolio_names'),
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
    products = products_query.all()

    print(products_query)
    products_with_portfolios = products_query.all()
    print(products_with_portfolios)

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
