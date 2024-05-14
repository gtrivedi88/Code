<fieldset class="product-log-group">
        <legend>Notes and changelog</legend>
        <div id="product-logs">
            {% for log in existing_logs %}
            <div class="product-log-pair" data-log-id="{{ log.log_id }}">
                <input type="hidden" name="existing_log_id" value="{{ log.log_id }}">
                <div class="form-field">
                    <label for="edit_notes_{{ log.log_id }}">{{ form.edit_notes.label }}</label>
                    <textarea name="edit_notes_{{ log.log_id }}" cols="40">{{ log.edit_notes }}</textarea>
                </div>
                <div class="form-field">
                    <label for="edit_date_{{ log.log_id }}">{{ form.edit_date.label }}</label>
                    <input type="date" name="edit_date_{{ log.log_id }}" value="{{ log.edit_date.strftime('%Y-%m-%d') }}">
                </div>
                <div class="form-field buttons-row">
                    <button type="button" class="remove-log" data-log-id="{{ log.log_id }}">Delete</button>
                </div>
            </div>
            {% endfor %}
        </div>
        <button type="button" id="add-log">Add log</button>
    </fieldset>
