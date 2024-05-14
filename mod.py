{% if product_partners %}
    <fieldset class="product-partner-group">
        <legend>Product partners information</legend>
        <label>In Partnership with</label>
        <div class="listview">
            <oll>
                {% for partner in product_partners | sort(attribute='partner.partner_name') %}
                <li>{{ partner.partner.partner_name }}</li>
                {% endfor %}
            </oll>
        </div>
    </fieldset>
    {% endif %}
