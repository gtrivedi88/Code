{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">{{ product.product_name }}</h1>
{% endblock %}

{% block content %}
{% if product %}
<div id="product-details">

    <!-- Date information -->
    <br>
    <div class="date-info">
        <b>Product created on:</b> {{ product.created.strftime('%B %d, %Y') }} <br>
        <b>Product last updated on:</b> {{ product.last_updated.strftime('%B %d, %Y') }}
    </div>
    
    <!-- Product Information -->

    {% if product.product_name or product_types or product.product_description or portfolios or
    product.product_notes.first() %}
    <fieldset class="product-information-group">
        <legend>Product information</legend>

        {% if product.product_name %}
        <div class="field-pair">
            <label>Product name</label>
            <span>{{ product.product_name }}</span>
        </div>
        {% endif %}

        {% if product_types %}
        <div class="field-pair">
            <label>Product type</label>
            <div class="listview">
                <oll>
                    {% for product_type in product_types %}
                    <li>{{ product_type.product_type }}</li>
                    {% endfor %}
                </oll>
            </div>
        </div>
        {% endif %}

        {% if product.product_description %}
        <div class="field-pair">
            <label>Product description</label>
            <span>{{ product.product_description }}</span>
        </div>
        {% endif %}

        {% if portfolios %}
        <div class="field-pair">
            <label>Portfolio</label>
            <div class="listview">
                <oll>
                    {% for portfolio in portfolios %}
                    <li>{{ portfolio.category_name }}</li>
                    {% endfor %}
                </oll>
            </div>
        </div>
        {% endif %}

        {% if product.product_notes.first() and product.product_notes.first().product_note %}
        <div class="field-pair">
            <label>Product notes</label>
            <span>{{ product.product_notes.first().product_note }}</span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product Parent/Components Information -->

    {% if sorted_product_components or sorted_child_components %}
    <fieldset class="product-component-section">
        <legend>Product taxonomy</legend>
        <div class="relationship-info">
            <!-- Product Parent Information -->
            {% if sorted_product_components %}
            <div class="parent-info">
                {% for component in sorted_product_components %}
                {% set component_name = component_product_names[component.product_id] %}
                {% if component_name %}
                <p>
                    {{ component.component_type | capitalize }} of <a
                        href="{{ url_for('view_routes.view_product_details', product_id=component.product_id) }}">
                        {{ component_name }}
                    </a>
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
            &nbsp;
            <!-- Child Components -->
            {% if sorted_child_components %}
            <div class="child-info">
                <span><b>Contains</b></span>
                {% for component in sorted_child_components %}
                {% set child_name = component_product_name[component.component_id] %}
                {% if child_name %}
                <p>
                    <a href="{{ url_for('view_routes.view_product_details', product_id=component.component_id) }}">
                        {{ child_name }}
                    </a> ({{ component.component_type }})
                </p>
                {% endif %}
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Reference Information -->

    {% if product_references %}
    <fieldset class="product-reference-group">
        <legend>Product reference information</legend>
        <div id="product-references">
            <div class="two-column-layout">
                <div class="column">
                    <label>Product reference</label>
                    {% for reference in product_references %}
                    {% if reference.product_link %}
                    <div class="field-pair">
                        <span><a href="{{ reference.product_link }}" target="_blank">{{ reference.product_link }}</a></span>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
                <div class="column">
                    <label>Reference description</label>
                    {% for reference in product_references %}
                    {% if reference.link_description %}
                    <div class="field-pair">
                        <span>{{ reference.link_description }}</span>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Status Details -->

    {% if product.deprecated or product.upcoming_change or product.product_status or product.product_status_detail %}
    <fieldset class="product-status-group">
        <legend>Product status information</legend>
        {% if product.deprecated %}
        <div class="field-pair">
            <label>Deprecated</label>
            <span>{{ "Yes" if product.deprecated else "No" }}</span>
        </div>
        {% endif %}

        {% if product.upcoming_change %}
        <div class="field-pair">
            <label>Upcoming change</label>
            <span>{{ "Yes" if product.upcoming_change else "No" }}</span>
        </div>
        {% endif %}

        {% if product.product_status %}
        <div class="field-pair">
            <label>Status</label>
            <span>{{ product.product_status }}</span>
        </div>
        {% endif %}

        {% if product.product_status_detail %}
        <div class="field-pair">
            <label>Status details</label>
            <span>{{ product.product_status_detail }}</span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product Alias Information -->

    {% if product_aliases %}
    <fieldset class="product-alias-section">
        <legend>Product alias information</legend>
        <p><b>Note:</b> Always use full product name on first use and whenever clarity is needed. After first use, you may use approved short
        forms or acronyms. Tech Docs (Technical, customer-facing documentation) refers to non-marketing, non-sales content used
        to train customers, assist with installation, etc., such as getting started guides, Jira/Bugzilla entries, and support
        case summaries.</p>
        <br>
        <div class="alias-table">
            <!-- Table Headers -->
            <div class="alias-table-header">
                <div class="alias-table-cell"><strong>Alias name</strong></div>
                <div class="alias-table-cell"><strong>Approved for general use</strong></div>
                <div class="alias-table-cell"><strong>Previous name</strong></div>
                <div class="alias-table-cell"><strong>Approved for tech docs</strong></div>
                <div class="alias-table-cell"><strong>Approved for tech docs code/cli</strong></div>
                <div class="alias-table-cell"><strong>Alias notes</strong></div>
            </div>
            <!-- Each Row Represents a Set of Alias Information -->
            {% for alias in product_aliases %}
            <div class="alias-table-row">
                <div class="alias-table-cell">{{ alias.alias_name }}</div>
                <div class="alias-table-cell">
                    {% if alias.alias_approved %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.previous_name %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.tech_docs %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.tech_docs_cli %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">{{ alias.alias_notes or "N/A" }}</div>
            </div>
            {% endfor %}
        </div>
    </fieldset>
    {% endif %}

    <!-- Product Release Information -->

    {% if product_mkt_life.product_release or product_mkt_life.product_release_detail or
    product_mkt_life.product_release_link %}
    <fieldset class="product-release-info">
        <legend>Product release information</legend>
        {% if product_mkt_life.product_release %}
        <div class="field-pair">
            <label>Release date</label>
            <span>{{ product_mkt_life.product_release.strftime('%m-%d-%Y') }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_release_detail %}
        <div class="field-pair">
            <label>Release detail</label>
            <span>{{ product_mkt_life.product_release_detail }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_release_link %}
        <div class="field-pair">
            <label>Release reference</label>
            <span><a href="{{ product_mkt_life.product_release_link }}" target="_blank">{{ product_mkt_life.product_release_link }}</a></span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product EOL Information -->

    {% if product_mkt_life.product_eol or product_mkt_life.product_eol_detail or product_mkt_life.product_eol_link %}
    <fieldset class="product-eol-info">
        <legend>Product end of life information</legend>
        {% if product_mkt_life.product_eol %}
        <div class="field-pair">
            <label>Product end of life (EOL) date</label>
            <span>{{ product_mkt_life.product_eol.strftime('%m-%d-%Y') }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_eol_detail %}
        <div class="field-pair">
            <label>Product end of life (EOL) details</label>
            <span>{{ product_mkt_life.product_eol_detail }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_eol_link %}
        <div class="field-pair">
            <label>Product end of life (EOL) reference</label>
            <span><a href="{{ product_mkt_life.product_eol_link }}" target="_blank">{{ product_mkt_life.product_eol_link }}</a></span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product Partners Information -->

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

    <!-- Product Notes Information -->

    {% if product_logs %}
    <fieldset class="product-notes-group">
        <legend>Notes and changelog</legend>
        <div id="product-notes" class="notes-table">
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Notes</th>
                        <th>Added By</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product_log in product_logs %}
                    <tr>
                        <td>{{ product_log.edit_date.strftime('%m-%d-%Y') }}</td>
                        <td>{{ product_log.edit_notes }}</td>
                        <td>{{ product_log.username }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </fieldset>
    {% endif %}
    
</div>
{% else %}
<p>No product details available.</p>
{% endif %}
<a href="{{ url_for('view_routes.view_products') }}" class="button-link">View more products</a> <a href="{{ url_for('edit_routes.edit_product_details', product_id=product.product_id) }}" class="button-link">Edit this
    product</a>
{% endblock %}
