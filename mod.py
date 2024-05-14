<fieldset class="product-partner-group">
        <legend>Product partners information</legend>
        <div class="form-field">
            <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
            <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                {% for value, label in form.partner.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
    </fieldset>
