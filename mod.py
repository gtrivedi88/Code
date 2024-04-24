{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Edit {{ product.product_name }}</h1>
{% endblock %}

{% block content %}
{% if not success_message %}
<p style="color:red;">Fields marked with * are mandatory.</p>

<!-- Display the edit form -->
<form method="post" action="{{ url_for('edit_routes.edit_product_details', product_id=product.product_id) }}">
    {{ form.hidden_tag() }}

    <!-- Date information -->
    <br>
    <div class="date-info">
        <b>Product created on:</b> {{ product.created.strftime('%B %d, %Y') }} <br>
        <b>Product last updated on:</b> {{ product.last_updated.strftime('%B %d, %Y') }}
    </div>


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

    <br>

    <fieldset class="product-reference-group">
        <legend>Product reference information</legend>
        <div id="product-references">
            {% for reference_form in reference_forms %}
            <div class="product-reference-pair">
                <div class="form-field">
                    <label for="{{ reference_form.product_link.id }}">{{ form.product_link.label }}</label>
                    {{ reference_form.product_link(cols=40) }}
                </div>

                <div class="form-field">
                    <label for="{{ reference_form.link_description.id }}">{{ form.link_description.label }}</label>
                    {{ reference_form.link_description(cols=40) }}
                </div>

                <div class="form-field buttons-row">
                    <button type="button" class="remove-reference">Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <button type="button" class="add-reference">
            {% if reference_forms %}
            Add more product reference information
            {% else %}
            Add reference information
            {% endif %}
        </button>
    </fieldset>

    <br>

    <fieldset class="product-status-group">
        <legend>Product status information</legend>
        <div class="form-group">
            <div class="checkbox-field">
                {{ form.deprecated() }}
                <label for="{{ form.deprecated.id }}">{{ form.deprecated.label }}</label>
            </div>

            <div class="checkbox-field">
                {{ form.upcoming_change() }}
                <label for="{{ form.upcoming_change.id }}">{{ form.upcoming_change.label }}</label>
            </div>
        </div>

        <br>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_status.id }}">Status</label>
                {{ form.product_status(id="status-dropdown", class="status-dropdown") }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_status_detail.id }}">Status details</label>
                {{ form.product_status_detail(id="status-details-dropdown", class="status-details-dropdown") }}
            </div>
        </div>
    </fieldset>

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

    <!-- Product Release Information -->
    <fieldset class="product-release-info">
        <legend>Product release information</legend>

        <label for="{{ form.product_release.id }}">{{ form.product_release.label }}</label>
        {{ form.product_release() }}

        <br>

        <label for="{{ form.product_release_detail.id }}">{{ form.product_release_detail.label }}</label>
        {{ form.product_release_detail(cols=40) }}

        <br>

        <label for="{{ form.product_release_link.id }}">{{ form.product_release_link.label }}</label>
        {{ form.product_release_link(cols=40) }}
    </fieldset>

    <!-- Product End of Life Information -->
    <fieldset class="product-eol-info">
        <legend>Product end of life information</legend>

        <label for="{{ form.product_eol.id }}">{{ form.product_eol.label }}</label>
        {{ form.product_eol() }}

        <br>

        <label for="{{ form.product_eol_detail.id }}">{{ form.product_eol_detail.label }}</label>
        {{ form.product_eol_detail(cols=40) }}

        <br>

        <label for="{{ form.product_eol_link.id }}">{{ form.product_eol_link.label }}</label>
        {{ form.product_eol_link(cols=40) }}
    </fieldset>

    <!-- Product Partners Information -->
    <fieldset class="product-partner-group">
        <legend>Product partners information</legend>
        <div class="form-field">
            <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
            <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                {% for value, label in form.partner.choices %}
                <option value="{{ value }}" {% if value in form.partner.data %} selected {% endif %}>{{ label }}
                </option>
                {% endfor %}
            </select>
        </div>
    </fieldset>

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
    
    

    <fieldset class="product-log-group">
        <legend>Notes and changelog</legend>
        <div id="product-logs">
            {% for log in existing_logs %}
            <div class="product-log-pair" data-log-id="{{ log.log_id }}">
                <input type="hidden" name="existing_log_id" value="{{ log.log_id }}">
                <div class="form-field">
                    <label for="edit_notes_{{ log.log_id }}">{{ form.edit_notes.label }}</label>
                    <textarea name="edit_notes_{{ log.log_id }}" cols="40">{{ log.edit_notes }}</textarea>
                </div>
                <div class="form-field">
                    <label for="edit_date_{{ log.log_id }}">{{ form.edit_date.label }}</label>
                    <input type="date" name="edit_date_{{ log.log_id }}" value="{{ log.edit_date.strftime('%Y-%m-%d') }}">
                </div>
                <div class="form-field buttons-row">
                    <button type="button" class="remove-log" data-log-id="{{ log.log_id }}">Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <button type="button" id="add-log">Add log</button>
    </fieldset>
    
    <!-- Placeholder for deleted log IDs -->
    <div id="deleted-logs"></div>

    {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 20px; padding: 10px; border: none;
    border-radius: 5px; cursor: pointer;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences_edit.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias_edit.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/component_edit.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/product_type.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/product_note.js') }}"></script>

{% endif %}

{% if success_message %}
<br>
<p class="success">{{ success_message|safe }}</p>
<br>
<a href="{{ url_for('edit_routes.edit_products') }}" class="button-link">Edit more products</a>
{% endif %}
{% endblock %}
