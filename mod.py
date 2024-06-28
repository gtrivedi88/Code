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
