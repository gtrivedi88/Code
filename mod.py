{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Add product</h1>
{% endblock %}

{% block content %}
{% if show_form %}

<p style="color:red;">Fields marked with * are mandatory.</p>

<form method="POST" action="{{ url_for('add_routes.add_product') }}" id="my-form">
    {{ form.hidden_tag() }}

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
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>


        <div class="form-group">

            <div class="form-field">
                <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
                {{ form.product_description(cols=40) }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
                <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
                    {% for value, label in form.product_portfolio.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_notes.id }}">{{ form.product_notes.label }}</label>
                {{ form.product_notes(cols=40) }}
            </div>
        </div>

    </fieldset>

    <fieldset class="product-reference-group">
            <legend>Product reference information</legend>
            <div id="product-references">
                <div class="product-reference-pair">
                    <div class="form-field">
                        <label for="{{ form.product_link.id }}">{{ form.product_link.label }}</label>
                        {{ form.product_link(cols=40) }}
                    </div>
        
                    <div class="form-field">
                        <label for="{{ form.link_description.id }}">{{ form.link_description.label }}</label>
                        {{ form.link_description(cols=40) }}
                    </div>
        
                    <div class="form-field buttons-row">
                        <button type="button" class="remove-reference">Delete</button>
                    </div>
                </div>
            </div>
            <button type="button" class="add-reference">
                {% if reference_forms %}
                Add more product reference information
                {% else %}
                Add reference information
                {% endif %}
            </button>
    </fieldset>



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
                <label for="{{ form.product_status.id }}">{{ form.product_status.label }}</label>
                {{ form.product_status(id="status-dropdown", class="status-dropdown") }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_status_detail.id }}">{{ form.product_status_detail.label }}</label>
                {{ form.product_status_detail(id="status-details-dropdown", class="status-details-dropdown") }}
            </div>
        </div>
    </fieldset>

    <fieldset class="product-alias-section">
        <legend>Product alias information</legend>
        <div id="product-aliases">
            <div class="product-alias-group">
                <div class="form-group">
                    <div class="form-field-inline">
                        <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
                        {{ form.alias_name(cols=30) }} <!-- Adjust column size as needed -->
                    </div>

                    <div class="form-field-inline">
                        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
                        {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
                    </div>

                    <div class="checkbox-group-inline">
                        <div class="checkbox-field">
                            <input type="checkbox" name="alias_approved" id="{{ form.alias_approved.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.alias_approved.id }}">{{ form.alias_approved.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="previous_name" id="{{ form.previous_name.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs" id="{{ form.tech_docs.id }}" class="alias-checkbox">
                            <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_cli" id="{{ form.tech_docs_cli.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
                        </div>
                    </div>

                    <div class="form-field-inline">
                        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
                        {{ form.alias_notes(cols=30) }}
                    </div>
                </div>
                <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
            </div>
        </div>
        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>

    </fieldset>

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

    <fieldset class="product-notes-group">
        <legend>Notes and changelog</legend>
        <div id="product-notes">
            <div class="product-notes-pair">
                <div class="form-field">
                    <label for="edit_date">Date</label>
                    <input type="date" id="edit_date" name="edit_date" value="{{ today }}">
                </div>
                <div class="form-field">
                    <label for="edit_notes"> {{ form.edit_notes.label }} </label>
                    <textarea id="edit_notes" name="edit_notes" cols="40"></textarea>
                </div>
            </div>
        </div>
    </fieldset>

    {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 20px; padding: 10px; border: none;
    border-radius: 5px; cursor: pointer;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/component.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/product_type.js') }}"></script>

{% endif %}

{% if success_message %}
<br>
<p class="success">{{ success_message|safe }}</p>
<br>
<a href="{{ url_for('add_routes.add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}
