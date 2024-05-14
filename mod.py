{% if product_logs %}
    <fieldset class="product-notes-group">
        <legend>Notes and changelog</legend>
        <div id="product-notes" class="notes-table">
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Notes</th>
                        <th>Added By</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product_log in product_logs %}
                    <tr>
                        <td>{{ product_log.edit_date.strftime('%m-%d-%Y') }}</td>
                        <td>{{ product_log.edit_notes }}</td>
                        <td>{{ product_log.username }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </fieldset>
    {% endif %}
