<fieldset class="pf-v5-c-form pf-m-horizontal">
        <legend class="pf-v5-c-title">Product status information</legend>
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-check">
                {{ form.deprecated() }}
                <label class="pf-v5-c-check__label" for="{{ form.deprecated.id }}">
                    {{ form.deprecated.label }}
                </label>
            </div>
            <div class="pf-v5-c-check">
                {{ form.upcoming_change() }}
                <label class="pf-v5-c-check__label" for="{{ form.upcoming_change.id }}">
                    {{ form.upcoming_change.label }}
                </label>
            </div>
        </div>
    
        <div class="pf-v5-c-form__group">
            <div class="pf-v5-c-form__group-control ">
                <label class="pf-v5-c-form__label" for="{{ form.product_status.id }}">
                    <span class="pf-v5-c-form__label-text">{{ form.product_status.label }}</span>
                </label>
                {{ form.product_status(id="status-dropdown", class="pf-v5-c-form-control") }}
            </div>
            <div class="pf-v5-c-form__group-control pf-m-mb-md">
                <label class="pf-v5-c-form__label" for="{{ form.product_status_detail.id }}">
                    <span class="pf-v5-c-form__label-text">{{
                    form.product_status_detail.label }}</span>
                </label>
                {{ form.product_status_detail(id="status-details-dropdown", class="pf-v5-c-form-control") }}
            </div>
        </div>
    </fieldset>
