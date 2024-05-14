<fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product information</legend>
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_name.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_name.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_name(class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>

            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_type.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_type.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <select class="pf-v5-c-form-control" id="{{ form.product_type.id }}"
                        name="{{ form.product_type.name }}" multiple>
                        {% for value, label in form.product_type.choices %}
                        <option value="{{ value }}">{{ label }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
        </div>

        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_description.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_description.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_description(class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>

            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_portfolio.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_portfolio.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    <select class="pf-v5-c-form-control" id="{{ form.product_portfolio.id }}"
                        name="{{ form.product_portfolio.name }}" multiple>
                        {% for value, label in form.product_portfolio.choices %}
                        <option value="{{ value }}">{{ label }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
        </div>

        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__field">
                <label class="pf-v5-c-form__label" for="{{ form.product_notes.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_notes.label }}</span>
                </label>
                <div class="pf-v5-c-form__field-control">
                    {{ form.product_notes(class="pf-v5-c-form-control", cols=40) }}
                </div>
            </div>
        </div>
    </fieldset>
