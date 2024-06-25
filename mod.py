<!doctype html>
{% include 'head.html' %}
<body>
  <div class="pf-v5-c-page">
    {% include 'masthead.html' %}
    {% include 'menu.html' %}
    <main class="pf-v5-c-page__main" tabindex="-1">
      <section class="pf-v5-c-page__main-section">
        {% block heading %}{% endblock %}
        {% block content %}{% endblock %}
      </section>
    </main>
  </div>
</body>


{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to the Official Product List Manager!</h1>
{% endblock %}

{% block content %}
<br>
<h3>{{ greeting }}, {{ first_name }}!</h3>
<h3>What would you like to do today?</h3>
<br><br>
<div class="tile-container">
    <!-- View Product Card -->
    <div class="pf-v5-c-card">
        <div class="pf-v5-c-card__header">
            <img src="{{ url_for('static', filename='/images/view_product.png') }}" class="pf-v5-c-card__img"
                alt="View Product">
        </div>
        <div class="pf-v5-c-card__body">
            <h4 class="pf-v5-c-title">View Product</h4>
            <p class="pf-v5-c-card__text">Explore the list of products.</p>
            <a href="opl/search-to-view-products" class="pf-v5-c-button pf-m-primary">View</a>
        </div>
    </div>

    {% if "/opl-editor" in needs.group %}
    <!-- Edit Product Card -->
    <div class="pf-v5-c-card">
        <div class="pf-v5-c-card__header">
            <img src="{{ url_for('static', filename='/images/edit_product.png') }}" class="pf-v5-c-card__img"
                alt="Edit Product">
        </div>
        <div class="pf-v5-c-card__body">
            <h4 class="pf-v5-c-title">Edit Product</h4>
            <p class="pf-v5-c-card__text">Modify existing product details.</p>
            <a href="opl/search-to-edit-products" class="pf-v5-c-button pf-m-secondary">Edit</a>
        </div>
    </div>
    {% endif %}

    {% if "/opl-editor" in needs.group %}
    <!-- Add Product Card -->
    <div class="pf-v5-c-card">
        <div class="pf-v5-c-card__header">
            <img src="{{ url_for('static', filename='/images/add_product.png') }}" class="pf-v5-c-card__img"
                alt="Add Product">
        </div>
        <div class="pf-v5-c-card__body">
            <h4 class="pf-v5-c-title">Add Product</h4>
            <p class="pf-v5-c-card__text">Introduce a new product to the list.</p>
            <a href="opl/add-product" class="pf-v5-c-button pf-m-tertiary">Add</a>
        </div>
    </div>
    {% endif %}
</div>

{% endblock %}



from flask import Blueprint, render_template, request
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




{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Search products</h1>
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
                {{ form.product_name(class="pf-v5-c-form-control") }}
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



{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">{{ product.product_name }}</h1>
{% endblock %}

{% block content %}
{% if product %}
<div id="product-details">

    <!-- Date information -->
    <div class="pf-v5-l-flex pf-m-row pf-m-align-items-center pf-m-justify-content-flex-end">
        <div class="pf-v5-c-card">
            <div class="pf-v5-c-card__body">
                <b>Product created on:</b> {{ product.created.strftime('%B %d, %Y') }}<br>
                <b>Product last updated on:</b> {{ product.last_updated.strftime('%B %d, %Y') }}
            </div>
        </div>
    </div>
    
    <!-- Product Information -->

    {% if product.product_name or product_types or product.product_description or portfolios or
    product.product_notes.first() %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product information</legend>

        {% if product.product_name %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Product name</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ product.product_name }}
            </div>
        </div>
        {% endif %}

        {% if product_types %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label"">
                <span class="pf-v5-c-form__label-text">Product type</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                <ul id="product_types" class="pf-v5-c-list">
                    {% for product_type in product_types %}
                    <li>{{ product_type.product_type }}</li>
                    {% endfor %}
                </ul>
        
            </div>
        </div>
        {% endif %}

        {% if product.product_description %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label"">
                            <span class=" pf-v5-c-form__label-text">Product description</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ product.product_description }}
            </div>
        </div>
        {% endif %}

        {% if portfolios %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Portfolio</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                <div class="pf-v5-c-form__control">
                    <ul id="portfolios" class="pf-v5-c-list">
                        {% for portfolio in portfolios %}
                        <li>{{ portfolio.category_name }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </div>
        {% endif %}

        {% if product.product_notes.first() and product.product_notes.first().product_note %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product notes</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ product.product_notes.first().product_note }}
                </div>
            </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product Parent/Components Information -->

    {% if sorted_product_components or sorted_child_components %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product taxonomy</legend>
        <div class="pf-v5-l-grid pf-m-gutter relationship-info">
            <!-- Product Parent Information -->
            {% if sorted_product_components %}
            <div class="pf-v5-l-grid__item pf-m-6-col parent-info">
                {% for component in sorted_product_components %}
                {% set component_name = component_product_names[component.product_id] %}
                {% if component_name %}
                <p>
                    {{ component.component_type | capitalize }} of
                    <a href="{{ url_for('view_routes.view_product_details', product_id=component.product_id) }}">
                        {{ component_name }}
                    </a>
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
    
            <!-- Child Components -->
            {% if sorted_child_components %}
            <div class="pf-v5-l-grid__item pf-m-6-col child-info">
                <span><b>Contains</b></span>
                {% for component in sorted_child_components %}
                {% set child_name = component_product_name[component.component_id] %}
                {% if child_name %}
                <p>
                    <a href="{{ url_for('view_routes.view_product_details', product_id=component.component_id) }}">
                        {{ child_name }}
                    </a> ({{ component.component_type }})
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Reference Information -->

    {% if product_references %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product reference information</legend>
        <div id="product-references" class="pf-v5-l-grid pf-m-gutter">
            <div class="pf-v5-l-grid__item pf-m-6-col">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product reference</span>
                </label>
            </div>
            <div class="pf-v5-l-grid__item pf-m-6-col">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Reference description</span>
                </label>
            </div>
        
            {% for reference in product_references %}
            <div class="pf-v5-l-grid__item pf-m-6-col">
                {% if reference.product_link %}
                <div class="pf-v5-c-form__field">
                    <span class="pf-v5-c-form__control product-reference-wrap">
                        <a href="{{ reference.product_link }}" target="_blank">{{ reference.product_link }}</a>
                    </span>
                </div>
                {% endif %}
            </div>
            <div class="pf-v5-l-grid__item pf-m-6-col">
                {% if reference.link_description %}
                <div class="pf-v5-c-form__field">
                    <span class="pf-v5-c-form__control product-reference-wrap">{{ reference.link_description }}</span>
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        </fieldset>
    {% endif %}

    <!-- Product Status Details -->

    {% if product.deprecated or product.upcoming_change or product.product_status or product.product_status_detail %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product status information</legend>
    
        {% if product.deprecated %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Deprecated</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ "Yes" if product.deprecated else "No" }}
            </div>
        </div>
        {% endif %}
    
        {% if product.upcoming_change %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Upcoming change</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ "Yes" if product.upcoming_change else "No"
                    }}
            </div>
        </div>
        {% endif %}
    
        {% if product.product_status %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Status</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ product.product_status }}
            </div>
        </div>
        {% endif %}
    
        {% if product.product_status_detail %}
        <div class="pf-v5-c-form__field">
            <label class="pf-v5-c-form__label">
                <span class="pf-v5-c-form__label-text">Status Details</span>
            </label>
            <div class="pf-v5-c-form__field-control">
                {{ product.product_status_detail }}
            </div>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product Alias Information -->

    {% if product_aliases %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product alias information</legend>
        <p><b>Note:</b> Always use full product name on first use and whenever clarity is needed. After first use, you may
            use approved short
            forms or acronyms. Tech Docs (Technical, customer-facing documentation) refers to non-marketing, non-sales
            content used
            to train customers, assist with installation, etc., such as getting started guides, Jira/Bugzilla entries, and
            support
            case summaries.</p>
        <div class="pf-v5-c-table pf-m-grid-md">
            <!-- Table Headers -->
            <div class="pf-v5-c-table__header">
                <div class="pf-v5-c-table__column"><strong>Alias name</strong></div>
                <div class="pf-v5-c-table__column"><strong>Approved for general use</strong></div>
                <div class="pf-v5-c-table__column"><strong>Previous name</strong></div>
                <div class="pf-v5-c-table__column"><strong>Approved for tech docs</strong></div>
                <div class="pf-v5-c-table__column"><strong>Approved for tech docs code/cli</strong></div>
                <div class="pf-v5-c-table__column"><strong>Alias notes</strong></div>
            </div>
            <!-- Each Row Represents a Set of Alias Information -->
            {% for alias in product_aliases %}
            <div class="pf-v5-c-table__row">
                <div class="pf-v5-c-table__column">{{ alias.alias_name }}</div>
                <div class="pf-v5-c-table__column">
                    {% if alias.alias_approved %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="pf-v5-c-table__column">
                    {% if alias.previous_name %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="pf-v5-c-table__column">
                    {% if alias.tech_docs %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="pf-v5-c-table__column">
                    {% if alias.tech_docs_cli %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="pf-v5-c-table__column">{{ alias.alias_notes or "N/A" }}</div>
            </div>
            {% endfor %}
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Release Information -->

    <div class="pf-v5-l-grid pf-m-gutter">
        {% if product_mkt_life.product_release or product_mkt_life.product_release_detail or
        product_mkt_life.product_release_link %}
        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product release information</legend>
    
            {% if product_mkt_life.product_release %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Release date</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                {{ product_mkt_life.product_release.strftime('%d %B %Y') }}
                </div>
            </div>
            {% endif %}
    
            {% if product_mkt_life.product_release_detail %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Release detail</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ product_mkt_life.product_release_detail }}
                </div>
            </div>
            {% endif %}
    
            {% if product_mkt_life.product_release_link %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Release reference</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <a href="{{ product_mkt_life.product_release_link }}" target="_blank">{{
                    product_mkt_life.product_release_link }}</a>
                </div>
            </div>
            {% endif %}
        </fieldset>
        {% endif %}
    
        <!-- Product EOL Information -->
        {% if product_mkt_life.product_eol or product_mkt_life.product_eol_detail or product_mkt_life.product_eol_link %}
        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product end of life information</legend>
    
            {% if product_mkt_life.product_eol %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product end of life (EOL) date</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                {{ product_mkt_life.product_eol.strftime('%d %B %Y') }}
                </div>
            </div>
            {% endif %}
    
            {% if product_mkt_life.product_eol_detail %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product end of life (EOL) details</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                {{ product_mkt_life.product_eol_detail }}
                </div>
            </div>
            {% endif %}
    
            {% if product_mkt_life.product_eol_link %}
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product end of life (EOL) reference</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                <a href="{{ product_mkt_life.product_eol_link }}" target="_blank">{{ product_mkt_life.product_eol_link
                    }}</a>
                    </div>
            </div>
            {% endif %}
        </fieldset>
    </div>
    {% endif %}

    <!-- Product Partners Information -->

    {% if product_partners %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product partners information</legend>
        <div class="pf-v5-c-form__field">
            <div class="pf-v5-c-form__group-control">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">In Partnership with</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <ul id="product_partners" class="pf-v5-c-list">
                        {% for partner in product_partners | sort(attribute='partner.partner_name') %}
                        <li>{{ partner.partner.partner_name }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Notes Information -->

    {% if product_logs %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Notes and changelog</legend>
        <div id="product-notes" class="pf-v5-c-table pf-m-grid-md">
            <div class="pf-v5-c-table__header">
                <div class="pf-v5-c-table__column"><strong>Date</strong></div>
                <div class="pf-v5-c-table__column"><strong>Notes</strong></div>
                <div class="pf-v5-c-table__column"><strong>Added By</strong></div>
            </div>
            <div class="pf-v5-c-table__body">
                {% for product_log in product_logs %}
                <div class="pf-v5-c-table__row">
                    <div class="pf-v5-c-table__column">{{ product_log.edit_date.strftime('%d %B %Y') }}</div>
                    <div class="pf-v5-c-table__column">{{ product_log.edit_notes }}</div>
                    <div class="pf-v5-c-table__column">{{ product_log.username }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </fieldset>
    {% endif %}
    
</div>
{% else %}
<p>No product details available.</p>
{% endif %}
<a href="{{ url_for('view_routes.view_products') }}" class="pf-v5-c-button pf-m-primary">View more products</a>
<a href="{{ url_for('edit_routes.edit_product_details', product_id=product.product_id) }}"
    class="pf-v5-c-button pf-m-primary">Edit this product</a>

{% endblock %}

<div class="pf-v5-c-page__sidebar">
  <div class="pf-v5-c-page__sidebar-body">
    <nav class="pf-v5-c-nav" aria-label="Global">
      <ul class="pf-v5-c-nav__list" role="list">
        <li class="pf-v5-c-nav__item">
          <a href="/"></a>
        </li>
        <li class="pf-v5-c-nav__item">
          <a href="/opl/search-to-view-products" class="pf-v5-c-nav__link">Search products</a>
        </li>
        {% if "/opl-editor" in needs.group %}
        <li class="pf-v5-c-nav__item">
          <a href="/opl/search-to-edit-products" class="pf-v5-c-nav__link">Edit product</a>
        </li>
        {% endif %}
        {% if "/opl-editor" in needs.group %}
        <li class="pf-v5-c-nav__item">
          <a href="/opl/add-product" class="pf-v5-c-nav__link">Add product</a>
        </li>
        {% endif %}
      </ul>
    </nav>
  </div>
</div>

