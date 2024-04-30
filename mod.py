{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Search products</h1>
{% endblock %}

{% block content %}
<script>
    function resetForm() {
        window.location.href = "{{ url_for('view_routes.reset_search_form') }}"; // Ensure this URL is correct
    }
</script>
<div class="container">
    <!-- Section 1: Search -->
    <fieldset class="product-search-group">
        <legend>Search by</legend>
        <div id="search-form" class="my-4">
            <form method="post" action="{{ url_for('view_routes.view_products') }}" class="form">
                {{ form.csrf_token }}
                {{ form.hidden_tag() }}

                <div class="form-group">
                    <label for="product_name">Product name</label>
                    {{ form.product_name(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_status">Product status</label>
                    {{ form.product_status(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_type">Product type</label>
                    {{ form.product_type(class="form-control") }}
                </div>

                {{ form.submit(class="button") }}
                <button type="button" class="button" onclick="resetForm()">Reset</button>
                

            </form>
        </div>
    </fieldset>

    <!-- Section 2: Search Results -->
    {% if form.is_submitted() and form.validate() %}
    <fieldset class="product-search-group">
        <legend>Search results</legend>
        <div id="search-results" class="my-4">
            {% if products_with_portfolios %}
            <ul class="list-unstyled">
                {% for product in products_with_portfolios %}
                <li class="mb-4 product-item">
                    <div class="product-info">
                        <h3 class="product-name">
                            <a href="{{ url_for('view_routes.view_product_details', product_id=product.product_id) }}">
                                {{ product.product_name }}
                            </a>
                        </h3>
                        <p class="product-status"><strong>Status:</strong> {{ product.product_status }}</p>
                        <p class="product-last-updated"><strong>Last Updated:</strong> {{
                            product.last_updated.strftime('%m-%d-%Y') }}</p>
                        {% if product.portfolio_names and product.portfolio_names|select('!=', None)|list|length > 0 %}
                        <p class="product-portfolios"><strong>Portfolios:</strong> {{ product.portfolio_names|join(', ') }}</p>
                        {% endif %}
                        <p class="product-types"><strong>Product Types:</strong> {{ ', '.join(product.product_types) }}
                        </p>
                    </div>
                </li>
                {% endfor %}
            </ul>
            {% else %}
            <p>No results found.</p>
            {% endif %}
        </div>
    </fieldset>
    {% endif %}
</div>
{% endblock %}




/* Heading */

.custom-heading {
    text-decoration: none;
    color: rgb(253, 253, 253);
   
}

.custom-heading:hover {
    text-decoration: none;
    color: rgb(241, 231, 231);
}

.custom-heading h1 {
    margin: 0;

}

/* Landing page */

h2 {
    font-size: 24px;
}

h3 {
    font-size: 19px;
}

h4 {
    font-size: 16px;
}

h5 {
    font-size: 13px;
}


/* Cards page */

.tile-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.card {
    border: 1px solid #ef6060;
    border-radius: 10px;
    overflow: hidden;
    width: 18rem;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-img-top {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    padding-top: 10px;
    padding-bottom: 10px;
}

.card-body {
    padding: 15px;
    background-color: #f8f9fa;
    border-top: 1px solid #eee;
}

.card-title {
    margin-bottom: 15px;
    font-size: 1.25rem;
}

.card-text {
    color: #555555;
    font-size: 15px;
    margin-bottom: 15px;
}

.btn {
    text-decoration: none;
    color: white;
    background-color: #007bff;
    padding: 10px 15px;
    border: none;
    border-radius: 0.25rem;
    font-size: 1em;
}

.btn:hover {
    background-color: #0056b3;
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* page */

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.checkbox-row {
    display: flex;
    align-items: center;
}

.checkbox-row input {
    margin-right: 10px;
}

.button-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #1a73e8;
    color: white;
    text-decoration: none;
    border-radius: 12px;
}

.success {
    color: green;
    font-weight: bold;
    font-size: 20px;
}

.product-reference-pair {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    border: 2px solid #31a795;
    padding: 10px;
    border-radius: 5px;
}

.form-group {
    display: flex;
}

.form-field {
    flex: 1 1 100%;
    
}

.checkbox-field {
    display: flex;
    flex: auto;
}

.checkbox-field input {
    margin-right: 10px;
    
}

.buttons-row {
    align-items: center;
    margin-top: 35px;
}

.buttons-row button {
    margin-left: 10px;
}

.remove-reference {
    background-color: #ff0000;
    color: white;
}

.remove-reference:hover {
    background-color: #cc0000;
}

.description {
    padding-bottom: 20px;
}

/* Alias information */

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

/* Product information border css */


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


/* Product Reference border css */

.product-reference-group {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }

.product-reference-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

/* Media query for smaller screens */
@media (max-width: 768px) {
    .product-reference-pair {
        border: 2px solid #31a795;
    }
}


.product-reference-pair .form-field {
    flex: 1 1 100%;
}

/* Media query for larger screens */
@media (min-width: 768px) {
    .product-reference-pair {
        flex-direction: row;
        align-items: flex-start;
        justify-content: space-between;
    }
}

/* Product Status border css */

.product-status-group {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }

.product-status-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}


/* Release information border css */

.product-release-info,
.product-eol-info,
.product-eol-info {
    width: 47.35%;
    display: inline-block;
    margin-right: 5%;
    border: 2px solid #0a63ca;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
}

.product-eol-info {
    margin-right: 0;
}

.product-release-info legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

.product-eol-info legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

/* Partner group */

.product-partner-group {
     border: 2px solid #0a63ca;
     padding: 10px;
     border-radius: 8px;
     margin-top: 10px;
 }


.product-partner-group legend {
     font-weight: bold;
     padding-left: 5px;
     padding-right: 5px;
 }


 /* component group */

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
    margin: 1em;
    margin-bottom: 2px;
 }

.product-component-group {
    border: 2px solid #31a795;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
    display:flex;
    flex-direction: column;
    overflow: hidden;
 }

 /* Adjust layout for larger screens */
 @media (min-width: 768px) {
     .product-component-group {
         flex-direction: row;
         justify-content: space-between;
         align-items: left;
     }

     .product-component-group .form-field {
         flex: 1;
         margin-right: 20px;
     }

     .product-component-group .form-field:last-child {
         margin-right: 0;
     }
 }

/* Styling for buttons and selects to ensure full width on smaller screens */
 .product-component-group select
 {
     width: 100%;
 }
 

 /* Product notes group */

 .product-notes-group {
     border: 2px solid #0a63ca;
     padding: 10px;
     border-radius: 8px;
     margin-top: 10px;
 }


 .product-notes-group legend {
     font-weight: bold;
     padding-left: 5px;
     padding-right: 5px;
 }

 .remove-notes {
     background-color: #ff0000;
     color: white;
 }

 .product-notes-pair {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    padding: 10px;
 }


.product-notes-pair .form-field {
     flex: 1 1 100%;
 }

 /* Media query for larger screens */
 @media (min-width: 768px) {
     .product-notes-pair {
         flex-direction: row;
         align-items: flex-start;
         justify-content: space-between;
     }
 }

/* Search css */

.product-search-group {
        border: 2px solid #0a63ca;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }


.product-search-group legend {
     font-weight: bold;
     font-size: 20px;
     padding-left: 5px;
     padding-right: 5px;
 }

 #search-results ul {
     list-style-type: none;
     padding: 0;
 }

 #search-results a {
     font-size: 1.2em;
     color: #007bff;
     text-decoration: none;
 }

 #search-results a:hover {
     text-decoration: underline;
 }

 .form-group {
    display: flex;
    flex-wrap: wrap;
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

 /* View form css */

 .field-pair {
     margin-bottom: 10px;
 }

 .field-pair label {
     font-weight: bold;
     margin-right: 10px;
 }

 .field-pair span {
     display: inline-block;

 }

 fieldset {
     border: 1px solid #ccc;
     padding: 10px;
     margin-bottom: 20px;
 }

 legend {
     font-weight: bold;
     font-size: 1.2em;
     padding-left: 5px;
     padding-right: 5px;
 }

 .two-column-layout {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
 }

 .column {
     flex-grow: 1;
 }

 .alias-columns {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    
 }

  /* Alias table css */

.alias-table {
    display: block;
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    white-space: wrap;
    
}

.alias-table-header,
.alias-table-row {
    display: table;
    width: 100%;
    table-layout: fixed;
    
}

.alias-table-cell {
    display: table-cell;
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
    word-wrap: break-word !important;
    hyphens: auto;
    
}

.alias-table-header .alias-table-cell,
.alias-table-row .alias-table-cell:first-child {
    font-weight: bold;
    background-color: #f2f2f2;
    
}

.alias-table-row:nth-child(odd) {
    background-color: #f9f9f9;
}

.alias-table-row:hover {
    background-color: #eaeaea;
}

.parent-columns,
.notes-columns {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}


/* Product notes css */

.product-log-pair {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    border: 2px solid #31a795;
    padding: 10px;
    border-radius: 5px;
}

.remove-log {
    background-color: #ff0000;
    color: white;
}

.remove-log:hover {
    background-color: #cc0000;
}

.product-log-group {
    border: 2px solid #0a63ca;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
    overflow-x: auto;
    }

.product-log-group legend {
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
}

/* Media query for smaller screens */
@media (max-width: 768px) {
    .product-log-pair {
        border: 2px solid #31a795;
    }
}


.product-log-pair .form-field {
    flex: 1 1 100%;
}

/* Media query for larger screens */
@media (min-width: 768px) {
    .product-log-pair {
        flex-direction: row;
        align-items: flex-start;
        justify-content: space-between;
    }
}


/* Log css */
.notes-table table {
    width: 100%;
    border-collapse: collapse;
}

.notes-table th,
.notes-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.notes-table th {
    background-color: #f2f2f2;
}

.notes-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.notes-table tr:hover {
    background-color: #e8f4ff;
}

/* last updated date */
.date-info {
    text-align: right;
    padding-right: 50px;
    
}

/* Custom CSS for product search results */
.product-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    background-color: #f9f9f9;
    transition: transform 0.3s ease-in-out;
}

.product-item:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 15px 0px rgba(0, 0, 0, 0.1);
}

.product-info {
    padding: 10px;
}

.product-name {
    font-size: 1.2em;
    margin-bottom: 5px;
    color: #333;
}

.product-status,
.product-portfolios,
.product-types,
.product-last-updated {
    margin-bottom: 5px;
}

.product-status strong,
.product-types strong,
.product-portfolios strong,
.product-last-updated strong {
    color: #666;
}

/* Animation for search form */
.product-search-group {
    transition: opacity 0.5s ease-in-out;
}

.product-search-group[disabled] {
    opacity: 0.5;
}


.button {
    background-color: #0a63ca;
    color: #ffffff;
    font-size: 17px;
    padding: 10px 20px;
    /* Uniform padding */
    border: none;
    border-radius: 5px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    /* Animation for hover effect */
}

.button:hover {
    background-color: #0056b3;
    /* Darker shade on hover */
    transform: scale(1.05);
    /* Slight increase in size */
}

.component-group,
.form-group,
.product-reference-group,
.product-log-group,
.product-information-group,
.product-alias-section,
.product-notes-group,
.product-status-group {
    
    flex-direction: column;
}

/* Media Query for larger screens - adjusts flex properties */
@media (min-width: 768px) {
    .form-group {
        flex-direction: row;
        justify-content: space-between;
    }

    .form-field {
        flex: 1 1 48%;
    }
}

.listview {

    padding-left: 25px;
}
