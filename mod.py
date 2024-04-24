<fieldset class="product-alias-section">
        <legend>Product alias information</legend>

        <!-- Existing Aliases -->
        <div id="existing-aliases">
            {% for alias in existing_aliases %}
            <div class="product-alias-group" id="alias-group-{{ alias.alias_id }}">
                <div class="form-group">
                    <div class="form-field-inline">
                        <label for="alias_name_{{ alias.alias_id }}">{{ form.alias_name.label }}</label>
                        <input type="text" name="alias_name_{{ alias.alias_id }}" value="{{ alias.alias_name }}" />
                    </div>

                    <div class="form-field-inline">
                        <label for="alias_type_{{ alias.alias_id }}">{{ form.alias_type.label }}</label>
                        <select name="alias_type_{{ alias.alias_id }}">
                            {% for value, label in form.alias_type.choices %}
                            <option value="{{ value }}" {% if value==alias.alias_type %}selected{% endif %}>{{ label }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="checkbox-group-inline">
                        <div class="checkbox-field">
                            <input type="checkbox" name="alias_approved_{{ alias.alias_id }}"
                                id="alias_approved_{{ alias.alias_id }}" {% if alias.alias_approved %} checked {% endif
                                %} />
                            <label for="alias_approved_{{ alias.alias_id }}">{{ form.alias_approved.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="previous_name_{{ alias.alias_id }}"
                                id="previous_name_{{ alias.alias_id }}" {% if alias.previous_name %} checked {% endif
                                %} />
                            <label for="previous_name_{{ alias.alias_id }}">{{ form.previous_name.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_{{ alias.alias_id }}"
                                id="tech_docs_{{ alias.alias_id }}" {% if alias.tech_docs %} checked {% endif %} />
                            <label for="tech_docs_{{ alias.alias_id }}">{{ form.tech_docs.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_cli_{{ alias.alias_id }}"
                                id="tech_docs_cli_{{ alias.alias_id }}" {% if alias.tech_docs_cli %} checked {% endif
                                %} />
                            <label for="tech_docs_cli_{{ alias.alias_id }}">{{ form.tech_docs_cli.label }}</label>
                        </div>
                    </div>

                    <div class="form-field-inline">
                        <label for="alias_notes_{{ alias.alias_id }}">{{ form.alias_notes.label }}</label>
                        <textarea name="alias_notes_{{ alias.alias_id }}" cols="30">{{ alias.alias_notes }}</textarea>
                    </div>
                </div>
                <button type="button" class="remove-alias-group">Delete alias</button>
            </div>
            {% endfor %}
        </div>

        <!-- Add More Aliases -->
        <div id="new-aliases">
            <!-- Template for New Alias Group -->
            <div class="product-alias-group template" style="display: none;">
                <div class="form-group">
                    <div class="form-field-inline">
                        <label for="alias_name_PLACEHOLDER">{{ form.alias_name.label }}</label>
                        <input type="text" name="alias_name_PLACEHOLDER" id="alias_name_PLACEHOLDER" cols="30" />
                    </div>

                    <div class="form-field-inline">
                        <label for="alias_type_PLACEHOLDER">{{ form.alias_type.label }}</label>
                        <select name="alias_type_PLACEHOLDER" id="alias_type_PLACEHOLDER">
                            {% for value, label in form.alias_type.choices %}
                            <option value="{{ value }}">{{ label }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="checkbox-group-inline">
                        <div class="checkbox-field">
                            <input type="checkbox" name="alias_approved_PLACEHOLDER" id="alias_approved_PLACEHOLDER" />
                            <label for="alias_approved_PLACEHOLDER">{{ form.alias_approved.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="previous_name_PLACEHOLDER" id="previous_name_PLACEHOLDER" />
                            <label for="previous_name_PLACEHOLDER">{{ form.previous_name.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_PLACEHOLDER" id="tech_docs_PLACEHOLDER" />
                            <label for="tech_docs_PLACEHOLDER">{{ form.tech_docs.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_cli_PLACEHOLDER" id="tech_docs_cli_PLACEHOLDER" />
                            <label for="tech_docs_cli_PLACEHOLDER">{{ form.tech_docs_cli.label }}</label>
                        </div>
                    </div>

                    <div class="form-field-inline">
                        <label for="alias_notes_PLACEHOLDER">{{ form.alias_notes.label }}</label>
                        <textarea name="alias_notes_PLACEHOLDER" id="alias_notes_PLACEHOLDER" cols="30"></textarea>
                    </div>
                </div>
                <button type="button" class="remove-alias-group">Delete</button>
            </div>
        </div>
        <br>
        <button type="button" class="add-alias-group">Add alias information</button>

    </fieldset>

.product-alias-group {
    border: 2px solid #31a795;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
    position: relative;
}

.product-alias-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

.remove-alias-group {
    background-color: #ff0000;
    color: white;
    margin-top: 10px;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.remove-alias-group:hover {
    background-color: #cc0000;
}

.form-field-inline,
.checkbox-group-inline {
    margin-right: 150px;
    display: flex;
    flex-direction: column;
    margin-top: 10px;
}

.checkbox-group-inline {
    display: flex;
    flex-direction: column;
    margin-top: 10px;
}

.product-alias-section {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        position: relative;
        overflow-x: auto;
    }
