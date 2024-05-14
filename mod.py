/* Log css */
.notes-table table {
    width: 100%;
    border-collapse: collapse;
}

.notes-table th,
.notes-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.notes-table th {
    background-color: #f2f2f2;
}

.notes-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.notes-table tr:hover {
    background-color: #e8f4ff;
}


{% if product_logs %}
    <fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Notes and changelog</legend>
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
