$(document).ready(function () {
    // Event listener for the change event on the product_status dropdown
    $('#status-dropdown').on('change', function () {
        updateStatusDetailsOptions();
        syncDeprecatedCheckbox();
    });

    // Event listener for the Deprecated checkbox
    $('#deprecated').on('change', function() {
        if ($(this).is(':checked')) {
            $('#status-dropdown').val('Deprecated');
            $('#status-details-dropdown').val('Null');
        } else {
            // Reset to original state when unchecked
            $('#status-dropdown').val('');
            $('#status-details-dropdown').val('');
            $('#status-details-dropdown').find('option').each(function () {
                $(this).prop('disabled', false);
            });
        }
        updateStatusDetailsOptions();
    });

    // Initial setup
    updateStatusDetailsOptions();
});

function updateStatusDetailsOptions() {
    var selectedStatus = $('#status-dropdown').val();
    var statusDetailsDropdown = $('#status-details-dropdown');

    // Disable or enable options based on the selected status
    if (selectedStatus === 'Available') {
        // Enable all options for 'Available'
        statusDetailsDropdown.find('option').each(function () {
            $(this).prop('disabled', false);
        });
     } else if (selectedStatus === 'Deprecated' || selectedStatus === 'Upcoming') {
        // Disable all options except 'NULL' for 'Deprecated' and 'Upcoming'
        statusDetailsDropdown.find('option').each(function () {
            if ($(this).val() !== 'Null' && $(this).val() !== 'Select') { 
                $(this).prop('disabled', true);
            }
        });
        statusDetailsDropdown.val('Null');
    } else {
        // If 'Select' or no value is selected, ensure 'Select' is the default and enable all options
        statusDetailsDropdown.val('');
        statusDetailsDropdown.find('option').each(function () {
            $(this).prop('disabled', false);
        });
    }
}

function syncDeprecatedCheckbox() {
    var selectedStatus = $('#status-dropdown').val();
    if (selectedStatus === 'Deprecated') {
        $('#deprecated').prop('checked', true);
    } else {
        $('#deprecated').prop('checked', false);
    }
}
