Successfully updated the product: <a href="/opl/product/a14b0aaa-00d9-4e37-bdad-0c145afdc0b4">3scale Backstage provider</a>

# Set success message and hide the form
            product_id=product_id
            view_link = url_for('view_routes.view_product_details', product_id=product_id)
            success_message = f'Successfully updated the product: <a href="{view_link}">{form.product_name.data}</a>'
            show_form = False
