from flask import Blueprint, render_template, request
from models import Product
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog

view_routes = Blueprint('view_routes', __name__)

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

    # Fetch the associated product components
    product_components = ProductComponents.query.filter_by(component_id=product_id).all()

    # Additional queries to retrieve product names based on component product_id
    component_product_names = {comp.product_id: Product.query.get(comp.product_id).product_name for comp in product_components}

    # Fetch the associated child components
    child_components = ProductComponents.query.filter_by(product_id=product_id).all()

    component_product_name = {comp.component_id: Product.query.get(comp.component_id).product_name for comp in child_components}

    # Fetch the associated product logs
    product_logs = ProductLog.query.filter_by(product_id=product_id).order_by(ProductLog.edit_date.desc()).all()
    
    return render_template('opl/view.html', 
                           product=product,
                           product_types=product_types,
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
