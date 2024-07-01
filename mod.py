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


{% extends 'base.html' %}

{% block heading %}
<h2 class="pf-v5-c-title pf-m-xl">Search products</h2>
{% endblock %}

{% block content %}
<script>
    function resetForm() {
        window.location.href = "{{ url_for('view_routes.reset_search_form') }}";
    }
</script>
<div class="pf-v5-c-page__main-section">
    <!-- Section 1: Search -->
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Search by</legend>
        <form method="post" action="{{ url_for('view_routes.view_products') }}">
            {{ form.csrf_token }}
            {{ form.hidden_tag() }}

            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="product_name">
                    <span class="pf-v5-c-form__label-text">Product name</span>
                </label>
                {{ form.product_name(class="pf-v5-c-form-control", value=request.args.get('product_name', '')) }}
            </div>

            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="product_status">
                    <span class="pf-v5-c-form__label-text">Product status</span>
                </label>
                {{ form.product_status(class="pf-v5-c-form-control") }}
            </div>

            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="product_type">
                    <span class="pf-v5-c-form__label-text">Product type</span>
                </label>
                {{ form.product_type(class="pf-v5-c-form-control") }}
            </div>

            <div class="pf-v5-c-form__actions">
                {{ form.submit(class="pf-v5-c-button pf-m-primary") }}
                <button type="button" class="pf-v5-c-button pf-m-secondary" onclick="resetForm()">Reset</button>
        </form>
</div>
</fieldset>

<!-- Section 2: Search Results -->
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
</div>
{% endblock %}
