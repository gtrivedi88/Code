<!-- Product Components Section -->
    <fieldset class="component-group">
        <legend>Product parent information</legend>
        <div id="components-container">
            {% for component in existing_components %}
            <div class="product-component-group">
                <div class="form-field">
                    <label for="product_id_{{ loop.index }}">{{ form.product_id.label }}</label>
                    <select name="product_id[]" id="product_id_{{ loop.index }}">
                        {% for value, label in form.product_id.choices %}
                        <option value="{{ value }}" {% if value==component.product_id %} selected {% endif %}>
                            {{ label }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
    
                <div class="form-field">
                    <label for="component_type_{{ loop.index }}">{{ form.component_type.label }}</label>
                    <select name="component_type[]" id="component_type_{{ loop.index }}">
                        {% for value, label in form.component_type.choices %}
                        <option value="{{ value }}" {% if value==component.component_type %} selected {% endif %}>
                            {{ label }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
                <button type="button" class="remove-component-group">Delete</button>
            </div>
            {% endfor %}
        </div>
        <!-- Hidden template for new product component groups -->
        <div id="product-component-template" style="display: none;">
            <div class="product-component-group">
                <div class="form-field">
                    <label>{{ form.product_id.label }}</label>
                    <select name="product_id[]" class="product_id-select">
                        {% for value, label in form.product_id.choices %}
                        <option value="{{ value }}">{{ label }}</option>
                        {% endfor %}
                    </select>
                </div>
        
                <div class="form-field">
                    <label>{{ form.component_type.label }}</label>
                    <select name="component_type[]" class="component-type-select">
                        {% for value, label in form.component_type.choices %}
                        <option value="{{ value }}">{{ label }}</option>
                        {% endfor %}
                    </select>
                </div>
                <button type="button" class="remove-component-group">Delete</button>
            </div>
        </div>
        <button type="button" class="add-component-group" style="margin-top: 10px;">Add more parent information</button>
    </fieldset>


    .component-group {
     border: 2px solid #0a63ca;
     padding: 10px;
     border-radius: 8px;
     margin-top: 10px;
 }

 .product-component-section {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }

.product-component-section legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}


 .product-component-group legend {
     font-weight: bold;
     padding-left: 5px;
     padding-right: 5px;
 }


 .remove-component-group {
    background-color: #ff0000;
    color: white;
 }

.product-component-group {
    border: 2px solid #31a795;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
 }
