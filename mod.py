# Fetch the associated product logs
    product_logs = ProductLog.query.filter_by(product_id=product_id).all()
