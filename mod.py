@view_routes.route('/opl/search-to-view-products', methods=['GET', 'POST'])
def view_products():
    # Initialize the search form
    form = SearchForm()

    # Define the base query for products, now including an order by clause
    products_query = Product.query.order_by(Product.product_name)

    # Filter products based on form data if the form is submitted and valid
    if form.validate_on_submit():
        if form.product_name.data:
            products_query = products_query.filter(Product.product_name.ilike(f"%{form.product_name.data}%"))

        if form.product_status.data and form.product_status.data != 'Select':
            products_query = products_query.filter(Product.product_status == form.product_status.data)

        if form.product_type.data and form.product_type.data:
            type_id = form.product_type.data
            if isinstance(type_id, list):
                type_id = type_id[0]  # Take the first item if it's a list, adjust according to your needs
            products_query = products_query.join(ProductTypeMap).join(ProductType).filter(ProductType.type_id == type_id)

    # Get the list of products based on the filtered and now sorted query
    products = products_query.all()

    # Check if a specific product is selected to display detailed information
    selected_product_id = request.args.get('product_id')
    selected_product = Product.query.get(selected_product_id) if selected_product_id else None

    return render_template('opl/view_search.html', form=form, products=products, selected_product=selected_product)
