<fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product Reference Information</legend>
        <div id="product-references" class="pf-v5-l-grid pf-m-gutter">
            <div class="pf-v5-l-grid__item pf-m-6-col">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Product Reference</span>
                </label>
            </div>
            <div class="pf-v5-l-grid__item pf-m-6-col">
                <label class="pf-v5-c-form__label">
                    <span class="pf-v5-c-form__label-text">Reference Description</span>
                </label>
            </div>
    
            {% for reference in product_references %}
            <div class="pf-v5-l-grid__item pf-m-6-col">
                {% if reference.product_link %}
                <div class="pf-v5-c-form__field">
                    <span class="pf-v5-c-form__control">
                        <a href="{{ reference.product_link }}" target="_blank">{{ reference.product_link }}</a>
                    </span>
                </div>
                {% endif %}
            </div>
            <div class="pf-v5-l-grid__item pf-m-6-col">
                {% if reference.link_description %}
                <div class="pf-v5-c-form__field">
                    <span class="pf-v5-c-form__control">{{ reference.link_description }}</span>
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
    </fieldset>
