{% if product.deprecated or product.upcoming_change or product.product_status or product.product_status_detail %}
    <fieldset class="product-status-group">
        <legend>Product status information</legend>
        {% if product.deprecated %}
        <div class="field-pair">
            <label>Deprecated</label>
            <span>{{ "Yes" if product.deprecated else "No" }}</span>
        </div>
        {% endif %}

        {% if product.upcoming_change %}
        <div class="field-pair">
            <label>Upcoming change</label>
            <span>{{ "Yes" if product.upcoming_change else "No" }}</span>
        </div>
        {% endif %}

        {% if product.product_status %}
        <div class="field-pair">
            <label>Status</label>
            <span>{{ product.product_status }}</span>
        </div>
        {% endif %}

        {% if product.product_status_detail %}
        <div class="field-pair">
            <label>Status details</label>
            <span>{{ product.product_status_detail }}</span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}
