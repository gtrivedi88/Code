<fieldset class="product-notes-group">
        <legend>Notes and changelog</legend>
        <div id="product-notes">
            <div class="product-notes-pair">
                <div class="form-field">
                    <label for="edit_date">Date</label>
                    <input type="date" id="edit_date" name="edit_date" value="{{ today }}">
                </div>
                <div class="form-field">
                    <label for="edit_notes"> {{ form.edit_notes.label }} </label>
                    <textarea id="edit_notes" name="edit_notes" cols="40"></textarea>
                </div>
            </div>
        </div>
    </fieldset>
