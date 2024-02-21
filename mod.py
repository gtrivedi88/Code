{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">{{ product.product_name }} Details</h1>
{% endblock %}

{% block content %}
{% if product %}
<div id="product-details">

    <!-- Product Information -->

    {% if product.product_name or product_types or product.product_description or portfolios or
    product.product_notes.first() %}
    <fieldset class="product-information-group">
        <legend>Product Information</legend>

        {% if product.product_name %}
        <div class="field-pair">
            <label>Product Name</label>
            <span>{{ product.product_name }}</span>
        </div>
        {% endif %}

        {% if product_types %}
        <div class="field-pair">
            <label>Product Type</label>
            <span>
                {% for product_type in product_types %}
                {{ product_type.product_type }}
                {% endfor %}
            </span>
        </div>
        {% endif %}

        {% if product.product_description %}
        <div class="field-pair">
            <label>Product Description</label>
            <span>{{ product.product_description }}</span>
        </div>
        {% endif %}

        {% if portfolios %}
        <div class="field-pair">
            <label>Member Of</label>
            <ul>
                {% for portfolio in portfolios %}
                <li>{{ portfolio.category_name }} portfolio</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        {% if product.product_notes.first() %}
        <div class="field-pair">
            <label>Product Notes</label>
            <span>{{ product.product_notes.first().product_note }}</span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}
