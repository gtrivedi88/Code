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



<div class="pf-v5-l-grid pf-m-gutter">
        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product release information</legend>
    
            <div class="pf-v5-c-form__group date">
                <label class="pf-v5-c-form__label" for="{{ form.product_release.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release.label }}</span>
                </label>
                {{ form.product_release(id=form.product_release.id, class="pf-v5-c-form-control") }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_release_detail.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release_detail.label }}</span>
                </label>
                {{ form.product_release_detail(id=form.product_release_detail.id, class="pf-v5-c-form-control", cols=40) }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_release_link.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_release_link.label }}</span>
                </label>
                {{ form.product_release_link(id=form.product_release_link.id, class="pf-v5-c-form-control", cols=40) }}
            </div>
        </fieldset>

        <fieldset class="pf-v5-c-form pf-m-horizontal pf-v5-l-grid__item pf-m-6-col">
            <legend class="pf-v5-c-title">Product end of life information</legend>
    
            <div class="pf-v5-c-form__group date">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol.label }}</span>
                </label>
                {{ form.product_eol(id=form.product_eol.id, class="pf-v5-c-form-control") }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol_detail.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol_detail.label }}</span>
                </label>
                {{ form.product_eol_detail(id=form.product_eol_detail.id, class="pf-v5-c-form-control", cols=40) }}
            </div>
    
            <div class="pf-v5-c-form__group">
                <label class="pf-v5-c-form__label" for="{{ form.product_eol_link.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_eol_link.label }}</span>
                </label>
                {{ form.product_eol_link(id=form.product_eol_link.id, class="pf-v5-c-form-control", cols=40) }}
            </div>
        </fieldset>
    </div>


from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog
import permissions

add_routes = Blueprint('add_routes', __name__)

@add_routes.route('/opl/add-product', methods=['GET', 'POST'])
@permissions.opl_editor_permission.require()
def add_product():
    form = MyForm()
    success_message = None
    show_form = True

    # Initialize the variables here
    today = datetime.utcnow().strftime('%Y-%m-%d')
    formatted_created_date = None
    formatted_last_updated_date = None

    # Populate product type choices
    form.product_type.choices = [(ptype.type_id, ptype.product_type) for ptype in ProductType.query.all()]

    # Populate product portfolio choices
    form.product_portfolio.choices = [(portfolio.category_id, portfolio.category_name) for portfolio in ProductPortfolios.query.all()]

    # Populate partner choices
    form.partner.choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Populate component choices with alphabetical sorting by product_name
    form.product_id.choices = [('', 'Select')] + [
        (str(product.product_id), product.product_name) for product in Product.query.order_by(Product.product_name).all()
    ]

    if form.validate_on_submit():
        # Logic for adding a new product
        created_date = datetime.now()
        print(request.form)

        # Create a new product instance
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            upcoming_change=form.upcoming_change.data,
            deprecated=form.deprecated.data,
            product_status=form.product_status.data if form.product_status.data != 'Select' else '',
            product_status_detail='NULL' if form.product_status.data == 'Deprecated' else form.product_status_detail.data,
            last_updated=created_date,
            created=created_date
        )

        # If product_status is Deprecated, set product_status_detail to 'NULL'
        if form.product_status.data == 'Deprecated':
                form.product_status_detail.data = 'NULL'


        # Add and commit the new product to the database
        db.session.add(new_product)
        db.session.commit()

        # Add product type mapping
        selected_product_types = form.product_type.data
        for product_type_id in selected_product_types:
            product_type_map = ProductTypeMap(product_id=new_product.product_id, type_id=product_type_id)
            db.session.add(product_type_map)

        # Add product portfolio mapping
        selected_portfolios = form.product_portfolio.data
        for portfolio_id in selected_portfolios:
            product_portfolio_map = ProductPortfolioMap(product_id=new_product.product_id, category_id=portfolio_id)
            db.session.add(product_portfolio_map)

        # Add Product Notes
        product_notes_data = form.product_notes.data
        if product_notes_data:
            product_notes = ProductNotes(product_id=new_product.product_id, product_note=product_notes_data)
            db.session.add(product_notes)

        # Add Product References
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
                product_id=new_product.product_id,
                product_link=reference_data['product_link'],
                link_description=reference_data['link_description']
            )
            db.session.add(product_references)

        # Process the first set of Product Alias fields
        alias_name = request.form.get('alias_name')
        if alias_name:
            alias_type = request.form.get('alias_type')
            alias_approved = 'alias_approved' in request.form  # Directly check for 'alias_approved'
            previous_name = 'previous_name' in request.form  # Directly check for 'previous_name'
            tech_docs = 'tech_docs' in request.form  # Directly check for 'tech_docs'
            tech_docs_cli = 'tech_docs_cli' in request.form  # Directly check for 'tech_docs_cli'
            alias_notes = request.form.get('alias_notes')

            first_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_name,
                alias_type=alias_type,
                alias_approved=alias_approved,
                previous_name=previous_name,
                tech_docs=tech_docs,
                tech_docs_cli=tech_docs_cli,
                alias_notes=alias_notes
            )
            db.session.add(first_alias)

        # Process subsequent sets of Product Alias fields
        alias_index = 2
        while True:
            alias_name_key = f'alias_name_{alias_index}'
            alias_name = request.form.get(alias_name_key)

            if not alias_name:
                break

            alias_type = request.form.get(f'alias_type_{alias_index}')
            alias_approved = f'alias_approved_{alias_index}' in request.form
            previous_name = f'previous_name_{alias_index}' in request.form
            tech_docs = f'tech_docs_{alias_index}' in request.form
            tech_docs_cli = f'tech_docs_cli_{alias_index}' in request.form
            alias_notes = request.form.get(f'alias_notes_{alias_index}')

            subsequent_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_name,
                alias_type=alias_type,
                alias_approved=alias_approved,
                previous_name=previous_name,
                tech_docs=tech_docs,
                tech_docs_cli=tech_docs_cli,
                alias_notes=alias_notes
            )
            db.session.add(subsequent_alias)
            alias_index += 1


        # Get the selected partner_id from the form
        selected_partner_ids = form.partner.data

        # Add product partners mapping
        for selected_partner_id in selected_partner_ids:
            product_partners = ProductPartners(
                product_id=new_product.product_id,
                partner_id=selected_partner_id
            )
            db.session.add(product_partners)


        # Add Product Components
        product_components_data = []
        product_ids = request.form.getlist('product_id')
        component_types = request.form.getlist('component_type')

        for i in range(len(product_ids)):
            product_id = product_ids[i]
            component_type = component_types[i]

            # Check if component_id is not 'Select'
            if product_id != 'Select':
                product_components_data.append({
                    'product_id': product_id,
                    'component_type': component_type
                })

        # Loop to save components
        for component_data in product_components_data:
            # Directly use boolean values, no need for lower()
            product_id = component_data['product_id']
            component_type = component_data['component_type']

            # Check if component_id is not 'Select' before saving to the database
            if product_id:
                # Create ProductComponent object and add to the session
                product_component = ProductComponents(
                    product_id=product_id,
                    component_id=new_product.product_id,
                    component_type=component_type
                )
                db.session.add(product_component)

        # Commit the changes to the database
        db.session.commit()


        # Add Product Mkt Life
        product_mkt_life = ProductMktLife(
            product_id=new_product.product_id,
            product_release=form.product_release.data,
            product_release_detail=form.product_release_detail.data,
            product_release_link=form.product_release_link.data,
            product_eol=form.product_eol.data,
            product_eol_detail=form.product_eol_detail.data,
            product_eol_link=form.product_eol_link.data
        )
        db.session.add(product_mkt_life)

        # Add product log
        edit_notes = request.form['edit_notes']
        edit_date_str = request.form.get('edit_date', '')
        username = "Gaurav"

        try:
            edit_date = datetime.strptime(edit_date_str, '%Y-%m-%d').date()
        except ValueError:
            edit_date = datetime.utcnow().date()  # Default to current date if parsing fails

        if edit_notes:
            product_log = ProductLog(
                product_id=new_product.product_id,
                edit_notes=edit_notes,
                edit_date=edit_date,
                username=username
            )
            db.session.add(product_log)

        # Commit changes outside the loop
        db.session.commit()

        # Format dates for display
        formatted_created_date = created_date.strftime('%Y-%m-%d')
        formatted_last_updated_date = created_date.strftime('%Y-%m-%d')

        # Set success message and hide the form

        view_link = url_for('view_routes.view_product_details', product_id=new_product.product_id)
        success_message = f'Successfully created the product: <a href="{view_link}">{form.product_name.data}</a>'
        show_form = False

    return render_template('opl/add.html', form=form, success_message=success_message,
                           show_form=show_form, formatted_created_date=formatted_created_date,
                           formatted_last_updated_date=formatted_last_updated_date, today=today)
