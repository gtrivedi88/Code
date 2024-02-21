@edit_routes.route('/opl/edit-product/<string:product_id>', methods=['GET', 'POST'])
def edit_product_details(product_id):
    print("Route accessed with method:", request.method)
    if request.method == 'POST':
        print("POST request received")
        print("Form data:", request.form)
    else:
        print("GET request received")
    product = Product.query.get_or_404(product_id)
    form = EditForm(obj=product)
    success_message = None
    show_form = True

    # Initialize the variables here
    last_updated_date = None
    formatted_last_updated_date = None
  
    if request.method == 'POST':
        if form.validate_on_submit() or 'submit' in request.form:
            # Logic for editing the product
            form.populate_obj(product)
            last_updated_date = datetime.now()

    # Check if last_updated_date has been set, then format it
    if last_updated_date:
        formatted_last_updated_date = last_updated_date.strftime('%Y-%m-%d')

    return render_template('opl/edit.html', form=form, product=product, success_message=success_message, show_form=show_form, formatted_last_updated_date=formatted_last_updated_date)
