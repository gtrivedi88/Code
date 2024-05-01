<fieldset class="product-reference-group">
            <legend>Product reference information</legend>
            <div id="product-references">
                <div class="product-reference-pair">
                    <div class="form-field">
                        <label for="{{ form.product_link.id }}">{{ form.product_link.label }}</label>
                        {{ form.product_link(cols=40) }}
                    </div>
        
                    <div class="form-field">
                        <label for="{{ form.link_description.id }}">{{ form.link_description.label }}</label>
                        {{ form.link_description(cols=40) }}
                    </div>
        
                    <div class="form-field buttons-row">
                        <button type="button" class="remove-reference">Delete</button>
                    </div>
                </div>
            </div>
            <button type="button" class="add-reference">
                {% if reference_forms %}
                Add more product reference information
                {% else %}
                Add reference information
                {% endif %}
            </button>
    </fieldset>

$(document).ready(function () {
    // Function to create a new reference pair
    function createNewReferencePair() {
        return $(`<div class="product-reference-pair">
            <div class="form-field">
                <label>Product reference</label>
                <textarea name="product_link" cols="40"></textarea>
            </div>
            <div class="form-field">
                <label>Reference description</label>
                <textarea name="link_description" cols="40"></textarea>
            </div>
            <div class="form-field buttons-row">
                <button type="button" class="remove-reference">Delete</button>
            </div>
        </div>`);
    }

    // Function to update the add-reference button text
    function updateAddReferenceButtonText() {
        if ($(".product-reference-pair").length === 0) {
            $(".add-reference").text("Add product reference information");
        } else {
            $(".add-reference").text("Add more product reference information");
        }
    }

    updateAddReferenceButtonText();

    $(".add-reference").click(function () {
        var referencePair = $(".product-reference-pair").length > 0 ? $(".product-reference-pair:first").clone() : createNewReferencePair();
        referencePair.find("input, textarea").val('');
        $("#product-references").append(referencePair);
        updateAddReferenceButtonText();
    });

    $(document).on("click", ".remove-reference", function () {
        $(this).closest(".product-reference-pair").remove();
        updateAddReferenceButtonText();
    });
});
