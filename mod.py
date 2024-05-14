{% if sorted_product_components or sorted_child_components %}
    <fieldset class="product-component-section">
        <legend>Product taxonomy</legend>
        <div class="relationship-info">
            <!-- Product Parent Information -->
            {% if sorted_product_components %}
            <div class="parent-info">
                {% for component in sorted_product_components %}
                {% set component_name = component_product_names[component.product_id] %}
                {% if component_name %}
                <p>
                    {{ component.component_type | capitalize }} of <a
                        href="{{ url_for('view_routes.view_product_details', product_id=component.product_id) }}">
                        {{ component_name }}
                    </a>
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
            &nbsp;
            <!-- Child Components -->
            {% if sorted_child_components %}
            <div class="child-info">
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
