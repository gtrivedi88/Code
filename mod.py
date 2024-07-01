# Route to view detailed information for a specific product
@view_routes.route('/opl/product/<string:product_id>', methods=['GET'])
def view_product_details(product_id):
    # Retrieve the product based on the provided product_id
    product = Product.query.get_or_404(product_id)

    if not product:
        # Handle the case where the product is not found
        return render_template('opl/view.html', product=None)

    # Fetch the associated product types
    product_types = ProductType.query.join(ProductTypeMap).filter_by(product_id=product_id).all()

    # Fetch the associated product portfolios
    product_portfolios = ProductPortfolioMap.query.filter_by(product_id=product_id).all()

    # Extract category_ids from the portfolio mappings
    category_ids = [portfolio.category_id for portfolio in product_portfolios]

    # Fetch the actual portfolios based on the category_ids
    portfolios = ProductPortfolios.query.filter(ProductPortfolios.category_id.in_(category_ids)).all()

    # Get partner choices
    partner_choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Get component choices
    component_choices = [('', 'Select')] + [(component.product_id, component.product_name) for component in Product.query.all()]

    # Get product notes
    product_notes = ProductNotes.query.filter_by(product_id=product_id).first()

    # Fetch the associated product references
    product_references = product.product_references.all()

    # Fetch the associated product aliases
    product_aliases = product.aliases.all()

    # Fetch the associated product release information
    product_mkt_life = ProductMktLife.query.filter_by(product_id=product_id).first()

    # Fetch the associated product partners
    product_partners = ProductPartners.query.filter_by(product_id=product_id).all()

    # Retrieve the parent and child components
    product_components = ProductComponents.query.filter_by(component_id=product_id).all()
    child_components = ProductComponents.query.filter_by(product_id=product_id).all()

    # Create dictionaries to store component names for sorting
    component_product_names = {comp.product_id: Product.query.get(comp.product_id).product_name for comp in product_components}
    component_product_name = {comp.component_id: Product.query.get(comp.component_id).product_name for comp in child_components}

    # Sort the components by the names stored in the dictionaries, case-insensitive
    sorted_product_components = sorted(product_components, key=lambda x: component_product_names.get(x.product_id, "").lower())
    sorted_child_components = sorted(child_components, key=lambda x: component_product_name.get(x.component_id, "").lower())


    # Fetch the associated product logs
    product_logs = ProductLog.query.filter_by(product_id=product_id).order_by(ProductLog.edit_date.desc()).all()

    return render_template('opl/view.html',
                           product=product,
                           product_types=product_types,
                           sorted_product_components=sorted_product_components,
                           sorted_child_components=sorted_child_components,
                           portfolios=portfolios,
                           partner_choices=partner_choices,
                           component_choices=component_choices,
                           product_notes=product_notes,
                           product_references=product_references,
                           product_aliases=product_aliases,
                           product_mkt_life=product_mkt_life,
                           product_partners=product_partners,
                           product_components=product_components,
                           child_components=child_components,
                           component_product_names=component_product_names,
                           component_product_name=component_product_name,
                           product_logs=product_logs)
