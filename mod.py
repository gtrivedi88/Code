{% extends 'base.html' %}

{% block heading %}
<h2 class="pf-v5-c-title pf-m-xl">Edit {{ product.product_name }}</h2>
{% endblock %}

{% block content %}
{% if not success_message %}

<!-- Display the edit form -->
<form method="post" action="{{ url_for('edit_routes.edit_product_details', product_id=product.product_id) }}">
    {{ form.hidden_tag() }}

    <!-- Date information -->
    <div class="pf-v5-l-flex pf-m-row pf-m-align-items-center pf-m-justify-content-flex-end">
        <div class="pf-v5-c-card">
            <div class="pf-v5-c-card__body">
                <b>Product created on:</b> {{ product.created.strftime('%B %d, %Y') }}<br>
                <b>Product last updated on:</b> {{ product.last_updated.strftime('%B %d, %Y') }}
            </div>
        </div>
    </div>
    <p class="pf-v5-c-alert pf-m-danger pf-m-inline" role="alert"><span class="pf-v5-c-alert__icon"><i
                class="fas fa-exclamation-circle" aria-hidden="true"></i></span> <strong>Fields marked with * are
            mandatory.</strong></p>


    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product information</legend>
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_name.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_name.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_name(id=form.product_name.id, class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_type.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_type.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" class="pf-v5-c-form-control"
                        multiple>
                        {% for value, label in form.product_type.choices %}
                        <option value="{{ value }}" {% if value in form.product_type.data %}selected{% endif %}>{{ label }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
            </div>
        </div>
    
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_description.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_description.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_description(id=form.product_description.id, class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_portfolio.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_portfolio.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}"
                        class="pf-v5-c-form-control" multiple>
                        {% for value, label in form.product_portfolio.choices %}
                        <option value="{{ value }}" {% if value in form.product_portfolio.data %}selected{% endif %}>{{
                            label }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
        </div>
    
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_note.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_note.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_note(id=form.product_note.id, class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>
        </div>
    </fieldset>

    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product reference information</legend>
        <div id="product-references">
            {% for reference_form in reference_forms %}
            <div class="pf-v5-c-form__group product-reference-pair">
                <div class="pf-v5-c-form__field">
                    <label class="pf-v5-c-form__label" for="{{ form.product_link.id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.product_link.label }}</span>
                    </label>
                    <div class="pf-v5-c-form__field-control">
                        {{ reference_form.product_link(class="pf-v5-c-form-control", cols=40) }}
                    </div>
                </div>
    
                <div class="pf-v5-c-form__field">
                    <label class="pf-v5-c-form__label" for="{{ form.link_description.id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.link_description.label }}</span>
                    </label>
                    <div class="pf-v5-c-form__field-control">
                        {{ reference_form.link_description(class="pf-v5-c-form-control", cols=40) }}
                    </div>
                </div>
    
                <div class="pf-v5-c-form__field">
                    <button type="button" class="pf-v5-c-button pf-m-danger remove-reference" style="margin-top: 45px;">
                        Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <button type="button" class="pf-v5-c-button pf-m-primary add-reference">
            {% if reference_forms %}
            Add more product reference information
            {% else %}
            Add reference information
            {% endif %}
        </button>
    </fieldset>
    <br>

    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product status information</legend>
        <div class="pf-v5-c-form__group">
            <!-- Use grid layout to handle checkbox alignment -->
            <div class="pf-v5-l-grid pf-m-all-6-col-on-sm pf-m-all-12-col">
                <div class="pf-v5-c-check pf-v5-l-grid__item">
                    {{ form.deprecated() }}
                    <label class="pf-v5-c-check__label" for="{{ form.deprecated.id }}">
                        {{ form.deprecated.label }}
                    </label>
                </div>
                <div class="pf-v5-c-check pf-v5-l-grid__item">
                    {{ form.upcoming_change() }}
                    <label class="pf-v5-c-check__label" for="{{ form.upcoming_change.id }}">
                        {{ form.upcoming_change.label }}
                    </label>
                </div>
            </div>
        </div>
    
        <div class="pf-v5-c-form__group">
    
            <div class="pf-v5-l-flex pf-m-column pf-m-row-on-md pf-m-align-items-flex-start pf-m-gap">
                <div class="pf-v5-c-form__group-control pf-v5-l-flex__item">
                    <label class="pf-v5-c-form__label" for="{{ form.product_status.id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.product_status.label }}</span>
                    </label>
                    {{ form.product_status(id="status-dropdown", class="pf-v5-c-form-control") }}
                </div>
                <div class="pf-v5-c-form__group-control pf-v5-l-flex__item">
                    <label class="pf-v5-c-form__label" for="{{ form.product_status_detail.id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.product_status_detail.label }}</span>
                    </label>
                    {{ form.product_status_detail(id="status-details-dropdown", class="pf-v5-c-form-control") }}
                </div>
            </div>
        </div>
    </fieldset>

    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product alias information</legend>
        <div id="product-aliases">
            {% for alias in existing_aliases %}
            <div class="product-alias-group pf-v5-c-form__group">
    
                <div class="pf-v5-l-grid pf-m-gutter">
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_name_{{ alias.alias_id }}">
                                <span class="pf-v5-c-form__label-text">{{ form.alias_name.label }}</span>
                            </label>
                            <input type="text" name="alias_name_{{ alias.alias_id }}" class="pf-v5-c-form-control"
                                value="{{ alias.alias_name }}" />
                        </div>
    
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_notes_{{ alias.alias_id }}">
                                <span class="pf-v5-c-form__label-text">{{ form.alias_notes.label }}</span>
                            </label>
                            <textarea name="alias_notes_{{ alias.alias_id }}" class="pf-v5-c-form-control"
                                cols="30">{{ alias.alias_notes }} </textarea>
                        </div>
                    </div>
    
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_type_{{ alias.alias_id }}>
                                <span class=" pf-v5-c-form__label-text">{{ form.alias_type.label }}</span>
                            </label>
                            <select class="pf-v5-c-form-control" name="alias_type_{{ alias.alias_id }}">
                                {% for value, label in form.alias_type.choices %}
                                <option value="{{ value }}" {% if value==alias.alias_type %}selected{% endif %}>{{ label }}
                                </option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
    
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <label class="pf-v5-c-form__label" for="{{ form.alias_type.id }}">
                            <span class="pf-v5-c-form__label-text">Is?</span>
                        </label>
                        <div class="pf-v5-c-form__group">
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" id="alias_approved_{{ alias.alias_id }}"
                                    name="alias_approved_{{ alias.alias_id }}" {% if alias.alias_approved %} checked {%
                                    endif %} />
                                <label class="pf-v5-c-check__label" for="alias_approved_{{ alias.alias_id }}">{{
                                    form.alias_approved.label }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input"
                                    name="previous_name_{{ alias.alias_id }}" id="previous_name_{{ alias.alias_id }}" {% if
                                    alias.previous_name %} checked {% endif %} />
                                <label class="pf-v5-c-check__label" for="previous_name_{{ alias.alias_id }}">{{
                                    form.previous_name.label }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_{{ alias.alias_id }}"
                                    id="tech_docs_{{ alias.alias_id }}" {% if alias.tech_docs %} checked {% endif %} />
                                <label class="pf-v5-c-check__label" for="tech_docs_{{ alias.alias_id }}">{{
                                    form.tech_docs.label
                                    }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input"
                                    name="tech_docs_cli_{{ alias.alias_id }}" id="tech_docs_cli_{{ alias.alias_id }}" {% if
                                    alias.tech_docs_cli %} checked {% endif %} />
                                <label class="pf-v5-c-check__label" for="tech_docs_cli_{{ alias.alias_id }}">{{
                                    form.tech_docs_cli.label }}</label>
                            </div>
                        </div>
                    </div>
                </div>
                <button type="button" class="pf-v5-c-button pf-m-danger remove-alias-group">Delete</button>
            </div>
            {% endfor %}
        </div>
        <div id="new-aliases">
            <!-- Template for New Alias Group -->
            <div class="product-alias-group template pf-v5-c-form__group" style="display:none;">
    
                <div class="pf-v5-l-grid pf-m-gutter">
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_name_PLACEHOLDER">
                                <span class="pf-v5-c-form__label-text">{{ form.alias_name.label }}</span>
                            </label>
                            <input type="text" name="alias_name_PLACEHOLDER" id="alias_name_PLACEHOLDER" cols="30"
                                class="pf-v5-c-form-control" />
                        </div>
    
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_notes_PLACEHOLDER">
                                <span class="pf-v5-c-form__label-text">{{ form.alias_notes.label }}</span>
                            </label>
                            <textarea name="alias_notes_PLACEHOLDER" id="alias_notes_PLACEHOLDER" cols="30"
                                class="pf-v5-c-form-control"> </textarea>
                        </div>
                    </div>
    
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <div class="pf-v5-c-form__group">
                            <label class="pf-v5-c-form__label" for="alias_type_PLACEHOLDER">
                                <span class="pf-v5-c-form__label-text">{{ form.alias_type.label }}</span>
                            </label>
                            <select class="pf-v5-c-form-control" name="alias_type_PLACEHOLDER" id="alias_type_PLACEHOLDER">
                                {% for value, label in form.alias_type.choices %}
                                <option value="{{ value }}">{{ label }}</option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
    
                    <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                        <label class="pf-v5-c-form__label" for="{{ form.alias_type.id }}">
                            <span class="pf-v5-c-form__label-text">Is?</span>
                        </label>
                        <div class="pf-v5-c-form__group">
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" name="alias_approved_PLACEHOLDER"
                                    id="alias_approved_PLACEHOLDER" />
                                <label class="pf-v5-c-check__label" for="alias_approved_PLACEHOLDER">{{
                                    form.alias_approved.label }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" name="previous_name_PLACEHOLDER"
                                    id="previous_name_PLACEHOLDER" />
                                <label class="pf-v5-c-check__label" for="previous_name_PLACEHOLDER">{{
                                    form.previous_name.label
                                    }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_PLACEHOLDER"
                                    id="tech_docs_PLACEHOLDER" />
                                <label class="pf-v5-c-check__label" for="tech_docs_PLACEHOLDER">{{ form.tech_docs.label
                                    }}</label>
                            </div>
                            <div class="pf-v5-c-check">
                                <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_cli_PLACEHOLDER"
                                    id="tech_docs_cli_PLACEHOLDER" />
                                <label class="pf-v5-c-check__label" for="tech_docs_cli_PLACEHOLDER">{{
                                    form.tech_docs_cli.label
                                    }}</label>
                            </div>
                        </div>
                    </div>
                </div>
                <button type="button" class="pf-v5-c-button pf-m-danger remove-alias-group">Delete</button>
            </div>
        </div>
        <button type="button" class="pf-v5-c-button pf-m-primary add-alias-group">Add more
            aliases</button>
    </fieldset>

    <!-- Product Release Information -->
    <div class="pf-v5-l-grid pf-m-gutter">
        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product release information</legend>
    
            <div class="pf-v5-c-form__group date">
                <label class="pf-v5-c-form__label" for="{{ form.product_release.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release.label }}</span>
                </label>
                {{ form.product_release(class="pf-v5-c-form-control") }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_release_detail.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release_detail.label }}</span>
                </label>
                {{ form.product_release_detail(class="pf-v5-c-form-control", cols=40) }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_release_link.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release_link.label }}</span>
                </label>
                {{ form.product_release_link(class="pf-v5-c-form-control", cols=40) }}
            </div>
        </fieldset>
    
        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product end of life information</legend>
    
            <div class="pf-v5-c-form__group date">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol.label }}</span>
                </label>
                {{ form.product_eol(class="pf-v5-c-form-control") }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol_detail.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol_detail.label }}</span>
                </label>
                {{ form.product_eol_detail(class="pf-v5-c-form-control", cols=40) }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol_link.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol_link.label }}</span>
                </label>
                {{ form.product_eol_link(class="pf-v5-c-form-control", cols=40) }}
            </div>
        </fieldset>
    </div>

    <!-- Product Partners Information -->
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product partners information</legend>
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__group-control">
                <label class="pf-v5-c-form__label" for="{{ form.partner.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.partner.label }}</span>
                </label>
                <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                    {% for value, label in form.partner.choices %}
                    <option value="{{ value }}" {% if value in form.partner.data %} selected {% endif %}>{{ label }}
                    </option>
                    {% endfor %}
                </select>
            </div>
        </div>
    </fieldset>

    <!-- Product Components Section -->
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product parent information</legend>
        <div id="product-component-groups">
            {% for component in existing_components %}
            <div class="product-component-group pf-v5-c-form__group">
                <div class="pf-v5-c-form__group-control">
                    <label class="pf-v5-c-form__label" for="product_id_{{ loop.index }}">
                        <span class="pf-v5-c-form__label-text">{{ form.product_id.label }}</span>
                    </label>
                    <select name="product_id[]" id="product_id_{{ loop.index }}" class="pf-v5-c-form-control">
                        {% for value, label in form.product_id.choices %}
                        <option value="{{ value }}" {% if value==component.product_id %} selected {% endif %}>
                            {{ label }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
    
                <div class="pf-v5-c-form__group-control">
                    <label class="pf-v5-c-form__label" for="component_type_{{ loop.index }}">
                        <span class="pf-v5-c-form__label-text">{{ form.component_type.label }}</span>
                    </label>
                    <select name="component_type[]" id="component_type_{{ loop.index }}" class="pf-v5-c-form-control">
                        {% for value, label in form.component_type.choices %}
                        <option value="{{ value }}" {% if value==component.component_type %} selected {% endif %}>
                            {{ label }}
                        </option>
                        {% endfor %}
                    </select>
                </div>
                <div class="pf-v5-c-form__field">
                    <button type="button" class="pf-v5-c-button pf-m-danger remove-component-group"
                        style="margin-top: 27px; ">Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <!-- Hidden template for new product component groups -->
        <div id="product-component-template" style="display: none;">
                <div class="product-component-group pf-v5-c-form__group">
                    <div class="pf-v5-c-form__group-control">
                        <label class="pf-v5-c-form__label" for="product_id[]">
                            <span class="pf-v5-c-form__label-text">{{ form.product_id.label }}</span>
                        </label>
                        <select name="product_id[]" class="pf-v5-c-form-control">
                            {% for value, label in form.product_id.choices %}
                            <option value="{{ value }}">
                                {{ label }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
    
                    <div class="pf-v5-c-form__group-control">
                        <label class="pf-v5-c-form__label" for="component_type[]">
                            <span class="pf-v5-c-form__label-text">{{ form.component_type.label }}</span>
                        </label>
                        <select name="component_type[]" class="pf-v5-c-form-control">
                            {% for value, label in form.component_type.choices %}
                            <option value="{{ value }}">{{ label }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    <div class="pf-v5-c-form__field">
                        <button type="button" class="pf-v5-c-button pf-m-danger remove-component-group"
                            style="margin-top: 27px; ">Delete</button>
                    </div>
                </div>
            </div>
            <button type="button" class="pf-v5-c-button pf-m-primary add-component-group">Add more parents</button>
    </fieldset>
    
    

    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Notes and changelog</legend>
        <div id="product-logs">
            {% for log in existing_logs %}
            <div class="product-log-pair pf-v5-c-form__group" data-log-id="{{ log.log_id }}">
                <input type="hidden" name="existing_log_id" value="{{ log.log_id }}">
    
                <!-- Notes Field -->
                <div class="pf-v5-c-form__group-control">
                    <label class="pf-v5-c-form__label" for="edit_notes_{{ log.log_id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.edit_notes.label }}</span>
                    </label>
                    <textarea name="edit_notes_{{ log.log_id }}" id="edit_notes_{{ log.log_id }}" class="pf-v5-c-form-control"
                        cols="40">{{ log.edit_notes }}</textarea>
                </div>
    
                <!-- Date Field -->
                <div class="pf-v5-c-form__group-control">
                    <label class="pf-v5-c-form__label" for="edit_date_{{ log.log_id }}">
                        <span class="pf-v5-c-form__label-text">{{ form.edit_date.label }}</span>
                    </label>
                    <input type="date" name="edit_date_{{ log.log_id }}" id="edit_date_{{ log.log_id }}"
                        class="pf-v5-c-form-control date" value="{{ log.edit_date.strftime('%Y-%m-%d') }}">
                </div>
    
                <!-- Buttons Row -->
                <div class="pf-v5-c-form__group-control buttons-row">
                    <button type="button" class="pf-v5-c-button pf-m-danger remove-log"
                        data-log-id="{{ log.log_id }}" style="margin-top: 30px;">Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <button type="button" id="add-log" class="pf-v5-c-button pf-m-primary">Add Log</button>
    </fieldset>
    
    <!-- Placeholder for deleted log IDs -->
    <div id="deleted-logs"></div>

    {{ form.submit(class="pf-v5-c-button pf-m-primary pf-m-display-lg") }}
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
<div class="pf-v5-c-alert pf-m-success" role="alert">
    <div class="pf-v5-c-alert__icon">
        <i class="fas fa-check-circle" aria-hidden="true"></i>
    </div>
    <h4 class="pf-v5-c-alert__title">{{ success_message|safe }}</h4>
</div>
<br>
<a href="{{ url_for('edit_routes.edit_products') }}" class="pf-v5-c-button pf-m-primary">Edit more products</a>
{% endif %}
{% endblock %}
