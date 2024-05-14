$(document).ready(function () {
    $('#add-log').click(function () {
        const newLogHTML = `
            <div class="product-log-pair">
                <div class="form-field">
                    <label>Product Log</label>
                    <textarea name="new_edit_notes" cols="40"></textarea>
                </div>
                <div class="form-field">
                    <label>Date</label>
                    <input type="date" name="new_edit_date" value="{{ now().strftime('%Y-%m-%d') }}">
                </div>
                <div class="form-field buttons-row">
                    <button type="button" class="remove-log">Remove</button>
                </div>
            </div>
        `;
        $('#product-logs').append(newLogHTML);
    });

    $(document).on('click', '.remove-log', function () {
        const logId = $(this).data('log-id');
        if (logId) {
            $('#deleted-logs').append(`<input type="hidden" name="deleted_log_ids" value="${logId}">`);
        }
        $(this).closest('.product-log-pair').remove();
    });
});
