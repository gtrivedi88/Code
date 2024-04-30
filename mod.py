{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Search products</h1>
{% endblock %}

{% block content %}
<script>
    function resetForm() {
        window.location.href = "{{ url_for('view_routes.reset_search_form') }}"; // Ensure this URL is correct
    }
</script>
<div class="container">
    <!-- Section 1: Search -->
    <fieldset class="product-search-group">
        <legend>Search by</legend>
        <div id="search-form" class="my-4">
            <form method="post" action="{{ url_for('view_routes.view_products') }}" class="form">
                {{ form.csrf_token }}
                {{ form.hidden_tag() }}

                <div class="form-group">
                    <label for="product_name">Product name</label>
                    {{ form.product_name(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_status">Product status</label>
                    {{ form.product_status(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_type">Product type</label>
                    {{ form.product_type(class="form-control") }}
                </div>

                {{ form.submit(class="button") }}
                <button type="button" class="button" onclick="resetForm()">Reset</button>
                

            </form>
        </div>
    </fieldset>

    <!-- Section 2: Search Results -->
    {% if form.is_submitted() and form.validate() %}
    <fieldset class="product-search-group">
        <legend>Search results</legend>
        <div id="search-results" class="my-4">
            {% if products_with_portfolios %}
            <ul class="list-unstyled">
                {% for product in products_with_portfolios %}
                <li class="mb-4 product-item">
                    <div class="product-info">
                        <h3 class="product-name">
                            <a href="{{ url_for('view_routes.view_product_details', product_id=product.product_id) }}">
                                {{ product.product_name }}
                            </a>
                        </h3>
                        <p class="product-status"><strong>Status:</strong> {{ product.product_status }}</p>
                        <p class="product-last-updated"><strong>Last Updated:</strong> {{
                            product.last_updated.strftime('%m-%d-%Y') }}</p>
                        {% if product.portfolio_names and product.portfolio_names|select('!=', None)|list|length > 0 %}
                        <p class="product-portfolios"><strong>Portfolios:</strong> {{ product.portfolio_names|join(', ') }}</p>
                        {% endif %}
                        <p class="product-types"><strong>Product Types:</strong> {{ ', '.join(product.product_types) }}
                        </p>
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
