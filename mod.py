product_mkt_life = ProductMktLife.query.get_or_404(product_id)

    # Populate the form with existing data
    if request.method == 'GET':
        form.product_release.data = product_mkt_life.product_release
        form.product_release_detail.data = product_mkt_life.product_release_detail
        form.product_release_link.data = product_mkt_life.product_release_link
        form.product_eol.data = product_mkt_life.product_eol
        form.product_eol_detail.data = product_mkt_life.product_eol_detail
        form.product_eol_link.data = product_mkt_life.product_eol_link

if form.validate_on_submit() or 'submit' in request.form:
        # Logic for editing the product
        print("New Aliases Data:", {key: value for key, value in request.form.items() if key.startswith('new_alias_')})
        form.populate_obj(product)
        product.last_updated = datetime.now()  # Update last_updated timestamp


# Update Product Market Life
        product_mkt_life.product_release = form.product_release.data
        product_mkt_life.product_release_detail = form.product_release_detail.data
        product_mkt_life.product_release_link = form.product_release_link.data
        product_mkt_life.product_eol = form.product_eol.data
        product_mkt_life.product_eol_detail = form.product_eol_detail.data
        product_mkt_life.product_eol_link = form.product_eol_link.data




# Fetch existing ProductMktLife data
    product_mkt_life = ProductMktLife.query.filter_by(product_id=product.product_id).first()
    if product_mkt_life:
        form.product_release.data = product_mkt_life.product_release
        form.product_release_detail.data = product_mkt_life.product_release_detail
        form.product_release_link.data = product_mkt_life.product_release_link
        form.product_eol.data = product_mkt_life.product_eol
        form.product_eol_detail.data = product_mkt_life.product_eol_detail
        form.product_eol_link.data = product_mkt_life.product_eol_link


if request.method == 'POST':
        if form.validate_on_submit() or 'submit' in request.form:
            # Logic for editing the product
            print("New Aliases Data:", {key: value for key, value in request.form.items() if key.startswith('new_alias_')})
            form.populate_obj(product)
            product.last_updated = datetime.now()

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
