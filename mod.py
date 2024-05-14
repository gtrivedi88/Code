{% if product_references %}
    <fieldset class="product-reference-group">
        <legend>Product reference information</legend>
        <div id="product-references">
            <div class="two-column-layout">
                <div class="column">
                    <label>Product reference</label>
                    {% for reference in product_references %}
                    {% if reference.product_link %}
                    <div class="field-pair">
                        <span><a href="{{ reference.product_link }}" target="_blank">{{ reference.product_link }}</a></span>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
                <div class="column">
                    <label>Reference description</label>
                    {% for reference in product_references %}
                    {% if reference.link_description %}
                    <div class="field-pair">
                        <span>{{ reference.link_description }}</span>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </fieldset>
    {% endif %}
