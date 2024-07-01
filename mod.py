from flask import Blueprint, render_template, request, jsonify
from models import Product
from sqlalchemy import or_
from sqlalchemy import func
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog

view_routes = Blueprint('view_routes', __name__)

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
        ProductPortfolios.category_name,
        ProductType.product_type
    ).outerjoin(ProductPortfolioMap, Product.product_id == ProductPortfolioMap.product_id) \
      .outerjoin(ProductPortfolios, ProductPortfolioMap.category_id == ProductPortfolios.category_id) \
      .join(ProductTypeMap, ProductTypeMap.product_id == Product.product_id) \
      .join(ProductType, ProductType.type_id == ProductTypeMap.type_id) \
      .outerjoin(ProductAlias, ProductAlias.product_id == Product.product_id) \
      .order_by(Product.product_name)

    # Handle search query from GET request
    search_query = request.args.get('product_name', '')
    if search_query:
        form.product_name.data = search_query
        search_term = f"%{search_query}%"
        products_query = products_query.filter(
            or_(
                Product.product_name.ilike(search_term),
                ProductAlias.alias_name.ilike(search_term)
            )
        )

    # Handle form submission
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

    # Process the results in Python
    product_dict = {}
    for product in products:
        product_id = product.product_id
        if product_id not in product_dict:
            product_dict[product_id] = {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_status': product.product_status,
                'last_updated': product.last_updated,
                'portfolio_names': set(),
                'product_types': set()
            }
        if product.category_name:
            product_dict[product_id]['portfolio_names'].add(product.category_name)
        if product.product_type:
            product_dict[product_id]['product_types'].add(product.product_type)

    # Convert sets to sorted lists
    products_with_portfolios = [
        {
            'product_id': prod['product_id'],
            'product_name': prod['product_name'],
            'product_status': prod['product_status'],
            'last_updated': prod['last_updated'],
            'portfolio_names': sorted(prod['portfolio_names']),
            'product_types': sorted(prod['product_types'])
        }
        for prod in product_dict.values()
    ]

    # Check if a specific product is selected to display detailed information
    selected_product_id = request.args.get('product_id')
    selected_product = Product.query.get(selected_product_id) if selected_product_id else None

    return render_template('opl/view_search.html', form=form, products=products, selected_product=selected_product, products_with_portfolios=products_with_portfolios)


# Flask route for resetting the form
@view_routes.route('/reset-view-search-form', methods=['GET'])
def reset_search_form():
    form = SearchForm()  # Creates a new form instance with default values
    return render_template('opl/view_search.html', form=form)


@view_routes.route('/opl/ajax-search', methods=['GET'])
def ajax_search():
    search_term = request.args.get('q', '')
    if not search_term:
        return jsonify([])

    search_term = f"%{search_term}%"
    products = Product.query.outerjoin(ProductAlias).filter(
        or_(Product.product_name.ilike(search_term),
            ProductAlias.alias_name.ilike(search_term))
    ).all()

    results = []
    for product in products:
        results.append({
            'id': product.product_id,
            'name': product.product_name
        })

    return jsonify(results)

# Route to view detailed information for a specific product
@view_routes.route('/opl/product/<string:product_id>', methods=['GET'])
def view_product_details(product_id):
    # Retrieve the product based on the provided product_id
    product = Product.query.get_or_404(product_id)

    if not product:
        # Handle the case where the product is not found
        return render_template('opl/view.html', product=None)

    # Fetch the associated product types
    product_types = ProductType.query.join(ProductTypeMap).filter_by(product_id=product_id).all()

    # Fetch the associated product portfolios
    product_portfolios = ProductPortfolioMap.query.filter_by(product_id=product_id).all()

    # Extract category_ids from the portfolio mappings
    category_ids = [portfolio.category_id for portfolio in product_portfolios]

    # Fetch the actual portfolios based on the category_ids
    portfolios = ProductPortfolios.query.filter(ProductPortfolios.category_id.in_(category_ids)).all()

    # Get partner choices
    partner_choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Get component choices
    component_choices = [('', 'Select')] + [(component.product_id, component.product_name) for component in Product.query.all()]

    # Get product notes
    product_notes = ProductNotes.query.filter_by(product_id=product_id).first()

    # Fetch the associated product references
    product_references = product.product_references.all()

    # Fetch the associated product aliases
    product_aliases = product.aliases.all()

    # Fetch the associated product release information
    product_mkt_life = ProductMktLife.query.filter_by(product_id=product_id).first()

    # Fetch the associated product partners
    product_partners = ProductPartners.query.filter_by(product_id=product_id).all()

    # Retrieve the parent and child components
    product_components = ProductComponents.query.filter_by(component_id=product_id).all()
    child_components = ProductComponents.query.filter_by(product_id=product_id).all()

    # Create dictionaries to store component names for sorting
    component_product_names = {comp.product_id: Product.query.get(comp.product_id).product_name for comp in product_components}
    component_product_name = {comp.component_id: Product.query.get(comp.component_id).product_name for comp in child_components}

    # Sort the components by the names stored in the dictionaries, case-insensitive
    sorted_product_components = sorted(product_components, key=lambda x: component_product_names.get(x.product_id, "").lower())
    sorted_child_components = sorted(child_components, key=lambda x: component_product_name.get(x.component_id, "").lower())


    # Fetch the associated product logs
    product_logs = ProductLog.query.filter_by(product_id=product_id).order_by(ProductLog.edit_date.desc()).all()

    return render_template('opl/view.html',
                           product=product,
                           product_types=product_types,
                           sorted_product_components=sorted_product_components,
                           sorted_child_components=sorted_child_components,
                           portfolios=portfolios,
                           partner_choices=partner_choices,
                           component_choices=component_choices,
                           product_notes=product_notes,
                           product_references=product_references,
                           product_aliases=product_aliases,
                           product_mkt_life=product_mkt_life,
                           product_partners=product_partners,
                           product_components=product_components,
                           child_components=child_components,
                           component_product_names=component_product_names,
                           component_product_name=component_product_name,
                           product_logs=product_logs)
