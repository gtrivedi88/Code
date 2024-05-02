<fieldset class="product-alias-section">
        <legend>Product alias information</legend>
        <div id="product-aliases">
            <div class="product-alias-group">
                <div class="form-group">
                    <div class="form-field-inline">
                        <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
                        {{ form.alias_name(cols=30) }} <!-- Adjust column size as needed -->
                    </div>

                    <div class="form-field-inline">
                        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
                        {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
                    </div>

                    <div class="checkbox-group-inline">
                        <div class="checkbox-field">
                            <input type="checkbox" name="alias_approved" id="{{ form.alias_approved.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.alias_approved.id }}">{{ form.alias_approved.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="previous_name" id="{{ form.previous_name.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs" id="{{ form.tech_docs.id }}" class="alias-checkbox">
                            <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
                        </div>

                        <div class="checkbox-field">
                            <input type="checkbox" name="tech_docs_cli" id="{{ form.tech_docs_cli.id }}"
                                class="alias-checkbox">
                            <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
                        </div>
                    </div>

                    <div class="form-field-inline">
                        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
                        {{ form.alias_notes(cols=30) }}
                    </div>
                </div>
                <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
            </div>
        </div>
        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>

    </fieldset>


    $(document).ready(function () {
    var aliasGroupIndex = 2; // Start with 2 for the first cloned group

    // Function to disable all checkboxes except the checked one
    function disableExceptChecked(aliasGroup, checkedCheckbox) {
        aliasGroup.find('input[type="checkbox"]').each(function () {
            if ($(this).attr('name') !== checkedCheckbox.attr('name')) {
                $(this).prop('disabled', true); // Disable all other checkboxes
            }
        });
    }

    // Function to enable all checkboxes
    function enableAllCheckboxes(aliasGroup) {
        aliasGroup.find('input[type="checkbox"]').prop('disabled', false);
    }

    // Function to reset alias_type dropdown to its original state
    function resetAliasTypeDropdown(aliasGroup) {
        aliasGroup.find('.alias-type-dropdown').val('').find('option').show();
    }

    // Updated adjustAliasTypeDropdown to include reset logic
    function adjustAliasTypeDropdown(aliasGroup, condition) {
        var aliasTypeDropdown = aliasGroup.find('.alias-type-dropdown');
        switch (condition) {
            case 'Former':
                aliasTypeDropdown.val('Former');
                break;
            case 'Cli':
                aliasTypeDropdown.val('Cli');
                break;
            case 'LimitToShortAndAcronym':
                aliasTypeDropdown.find('option').each(function() {
                    if ($(this).val() !== 'Short' && $(this).val() !== 'Acronym') {
                        $(this).hide();
                    } else {
                        $(this).show();
                    }
                });
                break;
            default:
                resetAliasTypeDropdown(aliasGroup);
                break;
        }
    }

    // Event listener for alias_type dropdown changes
    $('#product-aliases').on('change', '.alias-type-dropdown', function () {
        var aliasGroup = $(this).closest('.product-alias-group');
        enableAllCheckboxes(aliasGroup); // Re-enable all checkboxes on change
        var selectedValue = $(this).val();
        
        if (selectedValue === 'Cli') {
            aliasGroup.find('input[name^="tech_docs_cli"]').prop('checked', true).change();
        } else if (selectedValue === 'Former') {
            aliasGroup.find('input[name^="previous_name"]').prop('checked', true).change();
        }
    });

    // Event listener for checkbox changes
    $('#product-aliases').on('change', 'input[type="checkbox"]', function () {
        var aliasGroup = $(this).closest('.product-alias-group');
        var checkboxName = $(this).attr('name');
        var isChecked = $(this).is(':checked');

        if (isChecked) {
            disableExceptChecked(aliasGroup, $(this));
            // Apply specific logic based on the checkbox checked
            if (checkboxName.startsWith('tech_docs_cli')) {
                adjustAliasTypeDropdown(aliasGroup, 'Cli');
            } else if (checkboxName.startsWith('previous_name')) {
                adjustAliasTypeDropdown(aliasGroup, 'Former');
            } else if (checkboxName.startsWith('alias_approved') || checkboxName.startsWith('tech_docs')) {
                adjustAliasTypeDropdown(aliasGroup, 'LimitToShortAndAcronym');
            }
        } else {
            enableAllCheckboxes(aliasGroup);
            resetAliasTypeDropdown(aliasGroup); // Reset alias_type dropdown when any checkbox is unchecked
        }
    });

    // Add more Product Alias Information groups
    $(document).on("click", ".add-alias-group", function () {
        var newAliasGroup = $(".product-alias-group:first").clone();

        // Reset input and select values
        newAliasGroup.find('input[type="text"], select, textarea').val('');

        // Reset checkbox states and update names
        newAliasGroup.find('input, select, textarea').each(function() {
            if ($(this).attr('type') === 'checkbox') {
                $(this).prop('checked', false);
            }
            var originalName = $(this).attr('name');
            $(this).attr('name', originalName + '_' + aliasGroupIndex);
        });

        aliasGroupIndex++;  // Increment for the next group

        // Show remove button in the cloned group
        newAliasGroup.find('.remove-alias-group').show();

        // Append the new group inside the #product-aliases div
        $("#product-aliases").append(newAliasGroup);
    });

    // Remove the current Product Alias Information group
    $(document).on("click", ".remove-alias-group", function () {
        if ($(".product-alias-group").length > 1) {
            $(this).closest(".product-alias-group").remove();
        }
    });
});
