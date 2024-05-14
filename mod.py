<fieldset class="product-component-section">
        <legend>Product parent information</legend>
        <div class="product-component-group">
            <div class="form-field">
                <label for="{{ form.product_id.id }}">{{ form.product_id.label }}</label>
                <select id="{{ form.product_id.id }}" name="{{ form.product_id.name }}">
                    {% for value, label in form.product_id.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="form-field">
                <label for="{{ form.component_type.id }}">{{ form.component_type.label }}</label>
                <select id="{{ form.component_type.id }}" name="{{ form.component_type.name }}">
                    {% for value, label in form.component_type.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
            <button type="button" class="remove-component-group" style="display: none;">Delete</button>
        </div>
        <button type="button" class="add-component-group" style="margin-top: 10px;">Add more parents</button>

    </fieldset>
