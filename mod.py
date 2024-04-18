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
                    <button type="button" class="add-reference">Add more</button>
                    <button type="button" class="remove-reference" style="display: none;">Delete</button>
                </div>
            </div>
        </div>
    </fieldset>


$(document).ready(function () {
        // Add more Product Reference and Reference Description pairs
        $(".add-reference").click(function () {
            var referencePair = $(".product-reference-pair:first").clone();
            referencePair.find("input, textarea").val('');
            referencePair.find(".add-reference").hide();
            referencePair.find(".remove-reference").show();
            $("#product-references").append(referencePair);
        });

        // Remove the current Product Reference and Reference Description pair
        $(document).on("click", ".remove-reference", function () {
            $(this).closest(".product-reference-pair").remove();
        });
    });
