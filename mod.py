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


{% if portfolios %}
        <div class="field-pair">
            <label>Member Of</label>
            <ul>
                {% for portfolio in portfolios %}
                <li>{{ portfolio.category_name }} portfolio</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}



             {% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">View product details</h1>
{% endblock %}

{% block content %}
<div class="container">
    <!-- Section 1: Search -->
    <fieldset class="product-search-group">
        <legend>Search by</legend>
        <div id="search-form" class="my-4">
            <form method="post" action="{{ url_for('view_routes.view_products') }}" class="form">
                {{ form.csrf_token }}
                {{ form.hidden_tag() }}

                <div class="form-group">
                    <label for="product_name">Product Name:</label>
                    {{ form.product_name(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_status">Product Status:</label>
                    {{ form.product_status(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_type">Product Type</label>
                    {{ form.product_type(class="form-control") }}
                </div>

                {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 17px; padding-right: 10px;
                border: none; border-radius: 5px; font-weight: bold; cursor: pointer;") }}
                {{ form.reset(style="background-color: #0a63ca; color: #ffffff; font-size: 17px; padding-left: 10px;
                border: none; border-radius: 5px; font-weight: bold; cursor: pointer;") }}

            </form>
        </div>
    </fieldset>

    <!-- Section 2: Search Results -->
    {% if form.is_submitted() and form.validate() %}
    <fieldset class="product-search-group">
        <legend>Search Results</legend>
        <div id="search-results" class="my-4">
            {% if products %}
            <ul class="list-unstyled">
                {% for product in products %}
                <li class="mb-4 product-item">
                    <div class="product-info">
                        <h3 class="product-name">
                            <a href="{{ url_for('view_routes.view_product_details', product_id=product.product_id) }}">
                                {{ product.product_name }}
                            </a>
                        </h3>
                        <p class="product-status"><strong>Status:</strong> {{ product.product_status }}</p>
                        <p class="product-last-updated"><strong>Last Updated:</strong> {{ product.last_updated }}</p>
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
