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



    .product-information-group {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }

.product-information-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

.form-group {
     margin-bottom: 15px;
 }

 .form-group label {
     display: block;
     margin-bottom: 5px;
 }

 .form-group .form-control {
     width: 100%;
     padding: 8px;
     box-sizing: border-box;
     margin-bottom: 10px;
 }

 .form-group .btn {
     margin-right: 10px;
 }

 .form-field {
    flex: 1;
    
}

.form-field-inline,
.checkbox-group-inline {
    margin-right: 150px;
    display: flex;
    flex-direction: column;
    margin-top: 10px;
}
