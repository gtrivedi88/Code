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
    alias_type = SelectField('Alias type', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[Optional()])
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
    alias_type = SelectField('Alias type', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[Optional()])
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
