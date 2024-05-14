# Flask route for resetting the form
@edit_routes.route('/reset-search-form', methods=['GET'])
def reset_search_form():
    form = SearchForm()  # Creates a new form instance with default values
    return render_template('opl/edit_search.html', form=form)
