<fieldset class="product-information-group">
        <legend>Product information</legend>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_name.id }}">{{ form.product_name.label }}</label>
                {{ form.product_name(cols=40) }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_type.id }}">{{ form.product_type.label }}</label>
                <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" multiple>
                    {% for value, label in form.product_type.choices %}
                    <option value="{{ value }}" {% if value in form.product_type.data %}selected{% endif %}>{{ label }}
                    </option>
                    {% endfor %}
                </select>
            </div>

        </div>

        <br>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
                {{ form.product_description(cols=40) }}
            </div>


            <div class="form-field">
                <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
                <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
                    {% for value, label in form.product_portfolio.choices %}
                    <option value="{{ value }}" {% if value in form.product_portfolio.data %}selected{% endif %}>{{
                        label }}
                    </option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_note.id }}">{{ form.product_note.label }}</label>
                {{ form.product_note(cols=40) }}
            </div>
        </div>

    </fieldset>
