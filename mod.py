<!-- Product Parent/Components Information -->

    {% if product_components or child_components %}
    <fieldset class="product-component-section">
        <legend>Product taxonomy</legend>
        <div class="relationship-info">

            <!-- Product Parent Information -->
            {% if product_components %}
            <div class="parent-info">

                {% for component in product_components %}
                {% if component_product_names[component.product_id] and component.component_type %}
                <p>
                    {{ component.component_type | capitalize }} of <a
                        href="{{ url_for('view_routes.view_product_details', product_id=component.product_id) }}">{{
                        component_product_names[component.product_id] }}</a>
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
    
            {% if child_components %}
            <br>
            <div class="child-info">
                <span><b>Contains</b></span>
                {% for component in child_components %}
                {% if component_product_name[component.component_id] and component.component_type %}
                <p>
                    <a href="{{ url_for('view_routes.view_product_details', product_id=component.component_id) }}">{{
                        component_product_name[component.component_id] }}</a> ({{ component.component_type }})
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
    
        </div>
    </fieldset>
    {% endif %}
