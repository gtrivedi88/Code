{% if product.product_notes.first() %}
        <div class="field-pair">
            <label>Product notes</label>
            <span>{{ product.product_notes.first().product_note }}</span>
        </div>
        {% endif %}


# Get product notes
    product_notes = ProductNotes.query.filter_by(product_id=product_id).first()
