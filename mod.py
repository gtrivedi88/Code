# Delete existing ProductMktLife data
            existing_mkt_life = ProductMktLife.query.filter_by(product_id=product.product_id).first()
            if existing_mkt_life:
                print("Deleting existing ProductMktLife data")
                db.session.delete(existing_mkt_life)
                db.session.commit()

            If no existing data found run this

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

            If existing data found run this

            # Update Product Market Life
        product_mkt_life.product_release = form.product_release.data
        product_mkt_life.product_release_detail = form.product_release_detail.data
        product_mkt_life.product_release_link = form.product_release_link.data
        product_mkt_life.product_eol = form.product_eol.data
        product_mkt_life.product_eol_detail = form.product_eol_detail.data
        product_mkt_life.product_eol_link = form.product_eol_link.data
