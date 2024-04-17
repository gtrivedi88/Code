{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">View product details</h1>
{% endblock %}

{% block content %}
<div class="container">
    <!-- Section 1: Search -->
    <fieldset class="product-search-group">
        <legend>Search by</legend>
        <div id="search-form" class="my-4">
            <form method="post" action="{{ url_for('view_routes.view_products') }}" class="form">
                {{ form.csrf_token }}
                {{ form.hidden_tag() }}

                <div class="form-group">
                    <label for="product_name">Product Name:</label>
                    {{ form.product_name(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_status">Product Status:</label>
                    {{ form.product_status(class="form-control") }}
                </div>

                <div class="form-group">
                    <label for="product_type">Product Type:</label>
                    {{ form.product_type(class="form-control") }}
                </div>

                {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 17px; padding-right: 10px;
                border: none; border-radius: 5px; font-weight: bold; cursor: pointer;") }}
                {{ form.reset(style="background-color: #0a63ca; color: #ffffff; font-size: 17px; padding-left: 10px;
                border: none; border-radius: 5px; font-weight: bold; cursor: pointer;") }}
            </form>
        </div>
    </fieldset>



    class SearchForm(FlaskForm):
    product_name = StringField('Product Name')
    product_alias = StringField('Product Alias')
    product_portfolio = SelectMultipleField('Product Portfolio')
    product_status = SelectField('Product Status', choices=[('', 'Select'), ('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])
    submit = SubmitField('Search Product')
    product_type = SelectMultipleField('Product Type *')
    reset = SubmitField('Reset Form')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.product_type.choices = [(pt.type_id, pt.product_type) for pt in ProductType.query.all()]
