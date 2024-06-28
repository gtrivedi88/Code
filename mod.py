from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy import text
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog
import permissions

edit_routes = Blueprint('edit_routes', __name__)

@edit_routes.route('/opl/search-to-edit-products', methods=['GET', 'POST'])
@permissions.opl_editor_permission.require()
def edit_products():
    # Initialize the search form
    form = SearchForm()

    # Define the base query for products, including the portfolio name
    products_query = db.session.query(
        Product.product_id,
        Product.product_name,
        Product.product_status,
        Product.last_updated,
        ProductPortfolios.category_name,
        ProductType.product_type
    ).outerjoin(ProductPortfolioMap, Product.product_id == ProductPortfolioMap.product_id) \
      .outerjoin(ProductPortfolios, ProductPortfolioMap.category_id == ProductPortfolios.category_id) \
      .join(ProductTypeMap, ProductTypeMap.product_id == Product.product_id) \
      .join(ProductType, ProductType.type_id == ProductTypeMap.type_id) \
      .outerjoin(ProductAlias, ProductAlias.product_id == Product.product_id) \
      .order_by(Product.product_name)

    if form.validate_on_submit():
        if form.product_name.data:
            search_term = f"%{form.product_name.data}%"
            products_query = products_query.filter(
                or_(
                    Product.product_name.ilike(search_term),
                    ProductAlias.alias_name.ilike(search_term)
                )
            )
        if form.product_status.data and form.product_status.data != 'Select':
            products_query = products_query.filter(Product.product_status == form.product_status.data)
        if form.product_type.data and form.product_type.data:
            type_id = form.product_type.data
            if isinstance(type_id, list):
                type_id = type_id[0]
            products_query = products_query.filter(ProductType.type_id == type_id)

    # Get the list of products based on the filtered and now sorted query
    products = products_query.all()

    # Process the results in Python
    product_dict = {}
    for product in products:
        product_id = product.product_id
        if product_id not in product_dict:
            product_dict[product_id] = {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_status': product.product_status,
                'last_updated': product.last_updated,
                'portfolio_names': set(),
                'product_types': set()
            }
        if product.category_name:
            product_dict[product_id]['portfolio_names'].add(product.category_name)
        if product.product_type:
            product_dict[product_id]['product_types'].add(product.product_type)

    # Convert sets to sorted lists
    products_with_portfolios = [
        {
            'product_id': prod['product_id'],
            'product_name': prod['product_name'],
            'product_status': prod['product_status'],
            'last_updated': prod['last_updated'],
            'portfolio_names': sorted(prod['portfolio_names']),
            'product_types': sorted(prod['product_types'])
        }
        for prod in product_dict.values()
    ]

    # Check if a specific product is selected to display detailed information
    selected_product_id = request.args.get('product_id')
    selected_product = Product.query.get(selected_product_id) if selected_product_id else None

    return render_template('opl/edit_search.html', form=form, products=products, selected_product=selected_product, products_with_portfolios=products_with_portfolios)

# Flask route for resetting the form
@edit_routes.route('/reset-edit-search-form', methods=['GET'])
def reset_search_form():
    form = SearchForm()  # Creates a new form instance with default values
    return render_template('opl/edit_search.html', form=form)

@edit_routes.route('/opl/edit-product/<string:product_id>', methods=['GET', 'POST'])
@permissions.opl_editor_permission.require()
def edit_product_details(product_id):
    print("Route accessed with method:", request.method)
    if request.method == 'POST':
        print("POST request received")
        print("Form data:", request.form)
    else:
        print("GET request received")
    product = Product.query.get_or_404(product_id)
    product_notes = ProductNotes.query.filter_by(product_id=product_id).first()
    form = EditForm(obj=product)
    success_message = None
    show_form = True

    # Initialize the variables here
    last_updated_date = None
    formatted_last_updated_date = None

    # Populate the form with existing data
    if request.method == 'GET':
        # Only set product_note.data if product_notes exists
        form.product_note.data = product_notes.product_note if product_notes else ""


    # Fetch the associated product types
    product_types_map = ProductTypeMap.query.filter_by(product_id=product_id).all()

    # Get all available product types
    all_product_types = ProductType.query.all()

    # Populate product type choices
    form.product_type.choices = [(ptype.type_id, ptype.product_type) for ptype in all_product_types]

    # Set selected product types in the form
    form.product_type.data = [ptype_map.type_id for ptype_map in product_types_map]

    # Fetch the associated product portfolios
    product_portfolios_map = ProductPortfolioMap.query.filter_by(product_id=product_id).all()

    # Get all available product portfolios
    all_product_portfolios = ProductPortfolios.query.all()

    # Populate product portfolio choices
    form.product_portfolio.choices = [(portfolio.category_id, portfolio.category_name) for portfolio in all_product_portfolios]

    # Set selected product portfolios in the form
    form.product_portfolio.data = [pportfolio_map.category_id for pportfolio_map in product_portfolios_map]

    # Fetch existing product references for the product using raw SQL
    sql_query = text("SELECT * FROM brand_opl.product_references WHERE product_id = :product_id")
    existing_references = db.session.execute(sql_query, {"product_id": product_id}).fetchall()
    print("Existing References (SQL Query):", existing_references)

    # Create a form for each product reference
    reference_forms = [EditForm(obj=reference) for reference in existing_references]
    print("Reference Forms:", reference_forms)  # Add this line to print reference forms

    # Fetch existing product aliases
    existing_aliases = ProductAlias.query.filter_by(product_id=product_id).all()

    # Fetch existing ProductMktLife data
    product_mkt_life = ProductMktLife.query.filter_by(product_id=product.product_id).first()
    if product_mkt_life:
        form.product_release.data = product_mkt_life.product_release
        form.product_release_detail.data = product_mkt_life.product_release_detail
        form.product_release_link.data = product_mkt_life.product_release_link
        form.product_eol.data = product_mkt_life.product_eol
        form.product_eol_detail.data = product_mkt_life.product_eol_detail
        form.product_eol_link.data = product_mkt_life.product_eol_link

    # Fetch the associated product partners
    existing_product_partners = ProductPartners.query.filter_by(product_id=product_id).all()

    # Get all available partners
    all_partners = Partner.query.all()

    # Populate partner choices
    form.partner.choices = [(partner.partner_id, partner.partner_name) for partner in all_partners]

    # Set selected partners in the form
    form.partner.data = [ppartner.partner_id for ppartner in existing_product_partners]

    # Fetch existing product components for the product
    existing_components = ProductComponents.query.filter_by(component_id=product_id).all()

    # For GET or failed POST requests
    form.product_id.choices = [('', 'Select')] + [
        (str(prod.product_id), prod.product_name) for prod in Product.query.order_by(Product.product_name).all()
    ]

    # Fetch existing product logs for the product using raw SQL
    sql_query = text("SELECT * FROM brand_opl.product_log WHERE product_id = :product_id")
    existing_logs = db.session.execute(sql_query, {"product_id": product_id}).fetchall()


    if request.method == 'POST':
        if form.validate_on_submit() or 'submit' in request.form:
            # Logic for editing the product
            print("New Aliases Data:", {key: value for key, value in request.form.items() if key.startswith('new_alias_')})
            form.populate_obj(product)
            product.last_updated = datetime.now()

            # Product notes creation or update
            if not product_notes:
                product_notes = ProductNotes(product_id=product_id, product_note=form.product_note.data)
                db.session.add(product_notes)
            else:
                product_notes.product_note = form.product_note.data


            # Get the existing product types
            existing_product_type_ids = [ptype_map.type_id for ptype_map in product_types_map]

            # Get the selected product types
            selected_product_type_ids = request.form.getlist('product_type')

            # Add new product types
            for product_type_id in selected_product_type_ids:
                if product_type_id not in existing_product_type_ids:
                    new_product_type_map = ProductTypeMap(product_id=product.product_id, type_id=product_type_id)
                    db.session.add(new_product_type_map)

            # Remove unselected product types
            for ptype_map in product_types_map:
                if ptype_map.type_id not in selected_product_type_ids:
                    db.session.delete(ptype_map)

            # Get the existing product portfolios
            existing_product_portfolio_ids = [pportfolio_map.category_id for pportfolio_map in product_portfolios_map]

            # Get the selected product types and product portfolios
            selected_product_portfolio_ids = request.form.getlist('product_portfolio')

            # Add new product portfolios
            for product_portfolio_id in selected_product_portfolio_ids:
                if product_portfolio_id not in existing_product_portfolio_ids:
                    new_product_portfolio_map = ProductPortfolioMap(product_id=product.product_id, category_id=product_portfolio_id)
                    db.session.add(new_product_portfolio_map)

            # Remove unselected product portfolios
            for pportfolio_map in product_portfolios_map:
                if pportfolio_map.category_id not in selected_product_portfolio_ids:
                    db.session.delete(pportfolio_map)

            # Delete existing references for the product
            if existing_references:
                ProductReferences.query.filter_by(product_id=product.product_id).delete()

            # Add new references
            product_references_data = []
            for i in range(len(request.form.getlist('product_link'))):
                product_link = request.form.getlist('product_link')[i]
                link_description = request.form.getlist('link_description')[i]

                if product_link and link_description:
                    product_references_data.append({
                        'product_link': product_link,
                        'link_description': link_description
                    })

            for reference_data in product_references_data:
                product_references = ProductReferences(
                    product_id=product.product_id,
                    product_link=reference_data['product_link'],
                    link_description=reference_data['link_description']
                )
                db.session.add(product_references)

            # Update existing aliases
            for alias in existing_aliases:
                alias_name = request.form.get(f'alias_name_{alias.alias_id}')
                alias_type = request.form.get(f'alias_type_{alias.alias_id}')
                alias_approved = f'alias_approved_{alias.alias_id}' in request.form
                previous_name = f'previous_name_{alias.alias_id}' in request.form
                tech_docs = f'tech_docs_{alias.alias_id}' in request.form
                tech_docs_cli = f'tech_docs_cli_{alias.alias_id}' in request.form
                alias_notes = request.form.get(f'alias_notes_{alias.alias_id}')

                if alias_name:  # If alias exists, update it
                    alias.alias_name = alias_name
                    alias.alias_type = alias_type
                    alias.alias_approved = alias_approved
                    alias.previous_name = previous_name
                    alias.tech_docs = tech_docs
                    alias.tech_docs_cli = tech_docs_cli
                    alias.alias_notes = alias_notes
                else:  # If alias_name is not present, delete the alias
                    db.session.delete(alias)

            # Manual handling of new aliases
            new_aliases = []
            for key in request.form:
                if key.startswith('new_alias_name_'):
                    index = key.split('_')[-1]
                    new_alias = ProductAlias(
                        product_id=product_id,
                        alias_name=request.form.get(f'new_alias_name_{index}'),
                        alias_type=request.form.get(f'new_alias_type_{index}'),
                        alias_approved='new_alias_approved_' + index in request.form,
                        previous_name='new_previous_name_' + index in request.form,
                        tech_docs='new_tech_docs_' + index in request.form,
                        tech_docs_cli='new_tech_docs_cli_' + index in request.form,
                        alias_notes=request.form.get(f'new_alias_notes_{index}')
                    )
                    db.session.add(new_alias)


            # Update Product Mkt Life
            ProductMktLife.query.filter_by(product_id=product.product_id).delete()
            product_mkt_life = ProductMktLife(
                product_id=product.product_id,
                product_release=form.product_release.data,
                product_release_detail=form.product_release_detail.data,
                product_release_link=form.product_release_link.data,
                product_eol=form.product_eol.data,
                product_eol_detail=form.product_eol_detail.data,
                product_eol_link=form.product_eol_link.data
            )
            db.session.add(product_mkt_life)


            # Get the existing product partner ids
            existing_partner_ids = [ppartner.partner_id for ppartner in existing_product_partners]

            # Get the selected partners
            selected_partner_ids = request.form.getlist('partner')

            # Add new partners
            for partner_id in selected_partner_ids:
                if partner_id not in existing_partner_ids:
                    new_product_partner = ProductPartners(product_id=product.product_id, partner_id=partner_id)
                    db.session.add(new_product_partner)

            # Remove unselected partners
            for ppartner in existing_product_partners:
                if ppartner.partner_id not in selected_partner_ids:
                    db.session.delete(ppartner)

            # Existing component IDs for the product being edited
            existing_component_ids = [component.component_id for component in product.components]

            # Process submitted components
            parent_product_ids = request.form.getlist('product_id[]')
            component_types = request.form.getlist('component_type[]')

            # Remove all existing components not submitted
            ProductComponents.query.filter(
                ProductComponents.component_id == product_id,
                ProductComponents.product_id.notin_(parent_product_ids)
            ).delete(synchronize_session=False)

            # Update existing and add new components
            for parent_id, comp_type in zip(parent_product_ids, component_types):
                if parent_id and parent_id != 'Select':
                    existing_component = ProductComponents.query.filter_by(
                        component_id=product_id, product_id=parent_id
                    ).first()

                    if existing_component:
                        existing_component.component_type = comp_type
                    else:
                        db.session.add(ProductComponents(
                            component_id=product_id,
                            product_id=parent_id,
                            component_type=comp_type
                        ))

            # Handle deletions
            deleted_log_ids = request.form.getlist('deleted_log_ids')
            for log_id in deleted_log_ids:
                ProductLog.query.filter_by(log_id=log_id).delete()

            db.session.commit()  # Commit after deletions

            # Handle updates
            existing_log_ids = request.form.getlist('existing_log_id')
            for log_id in existing_log_ids:
                if log_id not in deleted_log_ids:  # Skip logs that are marked for deletion
                    log = ProductLog.query.filter_by(log_id=log_id, product_id=product_id).first()
                    if log:  # Check if log is not None
                        edit_notes_field = f'edit_notes_{log_id}'
                        edit_date_field = f'edit_date_{log_id}'
                        if edit_notes_field in request.form and edit_date_field in request.form:
                            log.edit_notes = request.form[edit_notes_field]
                            log.edit_date = datetime.strptime(request.form[edit_date_field], '%Y-%m-%d').date()
                            db.session.add(log)
                    else:
                        print(f"No log found for log_id: {log_id}")

            # Handle new logs
            new_edit_notes = request.form.getlist('new_edit_notes')
            new_edit_dates = request.form.getlist('new_edit_date')
            for notes, date_str in zip(new_edit_notes, new_edit_dates):
                if notes:
                    new_log_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else datetime.utcnow().date()
                    new_log = ProductLog(
                        product_id=product_id,
                        edit_notes=notes,
                        edit_date=new_log_date,
                        username="Gaurav"  # Ensure the username is handled as per your application's requirements
                    )
                    db.session.add(new_log)

            # Commit changes to the database
            try:
                db.session.commit()
            except Exception as e:
                print("Error during database commit:", e)
                db.session.rollback()


            # Set success message and hide the form
            product_id=product_id
            view_link = url_for('view_routes.view_product_details', product_id=product_id)
            success_message = f'Successfully updated the product: <a href="{view_link}">{form.product_name.data}</a>'
            show_form = False

    # Fetch the associated product references again as a list
    product_references = ProductReferences.query.filter_by(product_id=product_id).all()

    # Load existing logs for GET request
    existing_logs = ProductLog.query.filter_by(product_id=product_id).all()

    # Reload aliases to include new ones and reflect deletions
    existing_aliases = ProductAlias.query.filter_by(product_id=product_id).all()

    # For GET or failed POST requests
    form.product_id.choices = [('', 'Select')] + [
        (str(prod.product_id), prod.product_name) for prod in Product.query.order_by(Product.product_name).all()
    ]



    return render_template('opl/edit.html', form=form, product=product, success_message=success_message, show_form=show_form, existing_aliases=existing_aliases, reference_forms=reference_forms, existing_product_partners=existing_product_partners, existing_components=existing_components,formatted_last_updated_date=formatted_last_updated_date, existing_logs=existing_logs)




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



from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Product(db.Model):
    """
    Represents a product in the system.

    Attributes:
    - product_id: Unique identifier for the product, generated using UUID.
    - product_name: Name of the product.
    - product_description: Description of the product.
    - upcoming_change: Indicates if there is an upcoming change for the product.
    - deprecated: Indicates if the product is deprecated.
    - product_status: Status of the product.
    - last_updated: Date when the product was last updated.
    - created: Date when the product was created.
    - product_status_detail: Additional details about the product status.
    """

    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))

    # Relationships
    components = db.relationship('ProductComponents', back_populates='child_product', foreign_keys='[ProductComponents.component_id]')
    composed_of = db.relationship('ProductComponents', back_populates='parent_product', foreign_keys='[ProductComponents.product_id]')

class ProductType(db.Model):
    """
    Represents different types of products.

    Attributes:
    - type_id: Unique identifier for the product type.
    - product_type: Type of the product.
    """

    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

    # Relationships
    product_types_map = db.relationship('ProductTypeMap', back_populates='product_type')

class ProductTypeMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductType.

    Attributes:
    - product_id: Foreign key to Product.
    - type_id: Foreign key to ProductType.
    """

    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'),primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)

    # Relationships
    product_type = db.relationship('ProductType', back_populates='product_types_map')

class ProductPortfolios(db.Model):
    """
    Represents different portfolios for products.

    Attributes:
    - category_id: Unique identifier for the product portfolio.
    - category_name: Name of the product portfolio.
    """

    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "category_id"
    __term__ = "category_name"

    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='product_portfolio', lazy='dynamic')

class ProductPortfolioMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductPortfolios.

    Attributes:
    - product_id: Foreign key to Product.
    - category_id: Foreign key to ProductPortfolios.
    """

    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "category_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)

class ProductNotes(db.Model):
    """
    Represents notes associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_note: Note associated with the product.
    """

    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}


    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(65535), nullable=False)

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_notes', lazy='dynamic'))



class ProductReferences(db.Model):
    """
    Represents references associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_link: Link associated with the product reference.
    - link_description: Description associated with the product reference.

    Relationships:
    - product: Relationship to Product for easy access to the associated product references.
    """

    __tablename__ = 'product_references'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_link"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_link = db.Column(db.String(65535), nullable=False)
    link_description = db.Column(db.String(65535), nullable=False)

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_references', lazy='dynamic'))


class ProductAlias(db.Model):
    """
    Represents aliases associated with a product.

    Attributes:
    - alias_id: Unique identifier for the alias.
    - product_id: Foreign key to Product.
    - alias_name: Name associated with the alias.
    - alias_type: Type of the alias (Short, Acronym, Cli, Former).
    - alias_approved: Indicates if the alias is approved.
    - previous_name: Indicates if the alias is a previous name.
    - tech_docs: Indicates if the alias is approved for tech docs.
    - tech_docs_cli: Indicates if the alias is approved for tech docs code/CLI.
    - alias_notes: Notes associated with the alias.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_alias'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "alias_id"
    __term__ = "alias_name"

    alias_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), nullable=False)
    alias_name = db.Column(db.String(255), nullable=False)
    alias_type = db.Column(db.String(255), nullable=False)
    alias_approved = db.Column(db.Boolean, nullable=True)
    previous_name = db.Column(db.Boolean, nullable=True)
    tech_docs = db.Column(db.Boolean, nullable=True)
    tech_docs_cli = db.Column(db.Boolean, nullable=True)
    alias_notes = db.Column(db.String(65535))

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('aliases', lazy='dynamic'))


class ProductMktLife(db.Model):
    """
    Represents marketing life information for a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_release: Release date of the product.
    - product_release_detail: Details about the product release.
    - product_release_link: Reference link for the product release.
    - product_eol: End of Life date of the product.
    - product_eol_detail: Details about the End of Life of the product.
    - product_eol_link: Reference link for the End of Life of the product.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_mkt_life'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_release = db.Column(db.Date, nullable=True)
    product_release_detail = db.Column(db.String(255))
    product_release_link = db.Column(db.String(255))
    product_eol = db.Column(db.Date, nullable=True)
    product_eol_detail = db.Column(db.String(255))
    product_eol_link = db.Column(db.String(255))

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('mkt_life', lazy='dynamic'))


class Partner(db.Model):
    """
    Represents partners.

    Attributes:
    - partner_id: Unique identifier for the partner.
    - partner_name: Name of the partner.
    - persona_id: Persona ID for the partner.
    """

    __tablename__ = 'partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "partner_id"
    __term__ = "partner_name"

    partner_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_partners = db.relationship('ProductPartners', backref='partner', lazy='dynamic')

class ProductPartners(db.Model):
    """
    Represents a many-to-many relationship between Product and Partners.

    Attributes:
    - product_id: Foreign key to Product.
    - partner_id: Foreign key to Partners.
    """

    __tablename__ = 'product_partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "partner_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    partner_id = db.Column(db.String, db.ForeignKey('brand_opl.partners.partner_id'), primary_key=True)


class ProductComponents(db.Model):
    """
    Represents a many-to-many relationship between Product and Components.

    Attributes:
    - product_id: Foreign key to Product.
    - component_id: Foreign key to Components.
    """

    __tablename__ = 'product_components'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "component_id"

    component_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    component_type = db.Column(db.String(255), nullable=False)

    # Relationship back_populates
    child_product = db.relationship('Product', foreign_keys=[component_id], back_populates='components')
    parent_product = db.relationship('Product', foreign_keys=[product_id], back_populates='composed_of')


class ProductLog(db.Model):
    """
    Represents a log of changes made to a product.

    Attributes:
    - log_id: Unique identifier for the log entry.
    - product_id: Foreign key to Product.
    - edit_date: Date when the edit was made.
    - edit_notes: Notes associated with the edit.
    - username: Username of the user who made the edit.
    """

    __tablename__ = 'product_log'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "edit_date"

    log_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    edit_date = db.Column(db.Date, nullable=False)
    edit_notes = db.Column(db.String(65535), nullable=True)
    username = db.Column(db.String(255), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('ProductLog', lazy='dynamic'))




from flask_wtf import FlaskForm
from models import ProductType
from wtforms.validators import DataRequired, Optional, InputRequired
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, SelectMultipleField, DateField, HiddenField 

# Import DateField is duplicated, removed the second import
# from wtforms import DateField

# Below are the form classes for each taxonomy. Each is based on the wtforms
# specification. However, there are some additional variables to help with a
# few things:
#
#   form_choices        Used with forms that contain SelectField and
#                       SelectMultipleField. In some cases, the choices option
#                       for these two field types are usually taken from another
#                       table, which means they need to be set within the
#                       context of the Flask app. So this variable sets a
#                       mapping to data from another table, which the
#                       utils.get_choices_for_selectfields method renders and
#                       adds to the choices option of the relevant field. The
#                       mapping is as follows:
#                           'model'     The name of the model to pull data from.
#                           'value'     The column to use for the select field value
#                           'label'     The column to use for the select field label
#   mapped_data         This variable acts as a trigger to let the Flask app
#                       know that secondary table mapping is used. This is used
#                       to both get data and set data to the secondary table.

class MyForm(FlaskForm):
    product_name = TextAreaField('Product name *', validators=[DataRequired()])
    product_description = TextAreaField('Product description')
    upcoming_change = BooleanField('Upcoming change')
    deprecated = BooleanField('Deprecated')
    
    # SelectField for Product Status
    product_status = SelectField('Status', choices=[('', 'Select'), ('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status detail', choices=[('', 'Select'), ('General availability', 'General availability'), ('Live', 'Live'), ('Developer preview', 'Developer preview'), ('Technology preview', 'Technology preview'), ('Limited availability', 'Limited availability'), ('Service preview', 'Service preview'), ('Null', 'NULL')])

    # SelectField for Product Type
    product_type = SelectMultipleField('Product type *', validators=[InputRequired()])

    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')

    # Field for Product Notes
    product_notes = TextAreaField('Product notes')

    # Field for Product References
    product_link = TextAreaField('Product reference')
    link_description = TextAreaField('Reference description')

    # Fields for Product Alias
    alias_name = TextAreaField('Alias name')
    alias_type = SelectField('Alias type', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[InputRequired(Optional)])
    alias_approved = BooleanField('Alias approved')
    previous_name = BooleanField('Previous name')
    tech_docs = BooleanField('Approved for tech docs')
    tech_docs_cli = BooleanField('Approved for tech docs code/cLI')
    alias_notes = TextAreaField('Alias notes')

    # Fields for Product Mkt Life
    product_release = DateField('Release date', format='%Y-%m-%d', validators=[Optional()])
    product_release_detail = TextAreaField('Release detail')
    product_release_link = TextAreaField('Release reference')
    product_eol = DateField('Product end of life (EOL) date', format='%Y-%m-%d', validators=[Optional()])
    product_eol_detail = TextAreaField('Product end of life (EOL) details')
    product_eol_link = TextAreaField('Product end of life (EOL) reference')


    # Field for selecting a partner
    partner = SelectMultipleField('In partnership with', choices=[], coerce=str)

    # Field for selecting a component
    product_id = SelectField('Parent', choices=[('', 'Select')], validators=[Optional()])
    component_type = SelectField('Component type', choices=[('', 'Select'), ('component', 'Component'), ('feature', 'Feature'), ('tool', 'Tool'), ('add-on', 'Add-on'), ('operator', 'Operator'), ('variant', 'Variant')], validators=[Optional()])

    # Add a field to capture edit notes
    edit_date = DateField('Date')
    edit_notes = TextAreaField('Note')

    submit = SubmitField('Add product')


class SearchForm(FlaskForm):
    product_name = StringField('Product name')
    product_alias = StringField('Product alias')
    product_portfolio = SelectMultipleField('Product portfolio')
    product_status = SelectField('Product status', choices=[('', 'Select'), ('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])
    submit = SubmitField('Search', render_kw={'class': 'button'})
    product_type = SelectMultipleField('Product type *')
    reset = SubmitField('Reset Form')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.product_type.choices = [(pt.type_id, pt.product_type) for pt in ProductType.query.all()]

class EditForm(FlaskForm):
    # Add the necessary fields for editing
    product_name = TextAreaField('Product name *', validators=[DataRequired()])
    product_description = TextAreaField('Product description')
    upcoming_change = BooleanField('Upcoming change')
    deprecated = BooleanField('Deprecated')

    # SelectField for Product Type
    product_type = SelectMultipleField('Product type *', validators=[InputRequired()])

    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')

    # Field for Product References
    product_link = TextAreaField('Product reference')
    link_description = TextAreaField('Reference description')

    # SelectField for Product Status
    product_status = SelectField('Status', choices=[('', 'Select'), ('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status', choices=[('', 'Select'), ('General availability', 'General availability'), ('Live', 'Live'), ('Developer preview', 'Developer preview'), ('Technology preview', 'Technology preview'), ('Limited availability', 'Limited availability'), ('Service preview', 'Service preview'), ('Null', 'NULL')])
    
    # Add other fields as needed for editing
    
    submit = SubmitField('Save changes')

    # Fields for Product Alias
    alias_name = TextAreaField('Alias name')
    alias_type = SelectField('Alias type', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[InputRequired(Optional)])
    alias_approved = BooleanField('Approved for general use')
    previous_name = BooleanField('Previous name')
    tech_docs = BooleanField('Approved for tech docs')
    tech_docs_cli = BooleanField('Approved for tech docs code/cli')
    alias_notes = TextAreaField('Alias notes')

    # Fields for Product Mkt Life
    product_release = DateField('Release date', format='%Y-%m-%d', validators=[Optional()])
    product_release_detail = TextAreaField('Release detail')
    product_release_link = TextAreaField('Release reference')
    product_eol = DateField('Product end of life (EOL) date', format='%Y-%m-%d', validators=[Optional()])
    product_eol_detail = TextAreaField('Product end of life (EOL) details')
    product_eol_link = TextAreaField('Product end of life (EOL) reference')

    # Field for selecting a partner
    partner = SelectMultipleField('In partnership with', choices=[], coerce=str)

    # Field for selecting a component
    product_id = SelectField('Parent', choices=[('', 'Select')], validators=[Optional()])
    component_type = SelectField('Component type', choices=[('', 'Select'), ('component', 'Component'), ('feature', 'Feature'), ('tool', 'Tool'), ('add-on', 'Add-on'), ('operator', 'Operator'), ('variant', 'Variant')], validators=[Optional()])

    # Add a field to capture edit notes
    edit_date = DateField('Date')
    edit_notes = TextAreaField('Note')

    # Field for Product Notes
    product_note = TextAreaField('Product notes')
