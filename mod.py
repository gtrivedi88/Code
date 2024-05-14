<fieldset class="pf-v5-c-form pf-m-horizontal">
    <legend class="pf-v5-c-title">Product alias information</legend>
    <div id="product-aliases">
        {% for alias in existing_aliases %}
        <div class="product-alias-group pf-v5-c-form__group">

            <div class="pf-v5-l-grid pf-m-gutter">
                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_name_{{ alias.alias_id }}">
                            <span class="pf-v5-c-form__label-text">{{ form.alias_name.label }}</span>
                        </label>
                        <input type="text" name="alias_name_{{ alias.alias_id }}" class="pf-v5-c-form-control" value="{{ alias.alias_name }}" />
                    </div>

                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_notes_{{ alias.alias_id }}">
                            <span class="pf-v5-c-form__label-text">{{ form.alias_notes.label }}</span>
                        </label>
                        <textarea name="alias_notes_{{ alias.alias_id }}" class="pf-v5-c-form-control" cols="30">{{ alias.alias_notes }} </textarea>
                    </div>
                </div>

                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_type_{{ alias.alias_id }}>
                            <span class="pf-v5-c-form__label-text">{{ form.alias_type.label }}</span>
                        </label>
                        <select class="pf-v5-c-form-control" name="alias_type_{{ alias.alias_id }}">
                            {% for value, label in form.alias_type.choices %}
                            <option value="{{ value }}" {% if value==alias.alias_type %}selected{% endif %}>{{ label }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                </div>

                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <label class="pf-v5-c-form__label" for="{{ form.alias_type.id }}">
                        <span class="pf-v5-c-form__label-text">Is?</span>
                    </label>
                    <div class="pf-v5-c-form__group">
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" id="alias_approved_{{ alias.alias_id }}" name="alias_approved_{{ alias.alias_id }}" {% if alias.alias_approved %} checked {% endif
                                %} />
                            <label class="pf-v5-c-check__label" for="alias_approved_{{ alias.alias_id }}">{{
                                form.alias_approved.label }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="previous_name_{{ alias.alias_id }}"
                                id="previous_name_{{ alias.alias_id }}" {% if alias.previous_name %} checked {% endif
                                %} />
                            <label class="pf-v5-c-check__label" for="previous_name_{{ alias.alias_id }}">{{
                                form.previous_name.label }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_{{ alias.alias_id }}"
                                id="tech_docs_{{ alias.alias_id }}" {% if alias.tech_docs %} checked {% endif %} />
                            <label class="pf-v5-c-check__label" for="tech_docs_{{ alias.alias_id }}">{{ form.tech_docs.label
                                }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_cli_{{ alias.alias_id }}"
                                id="tech_docs_cli_{{ alias.alias_id }}" {% if alias.tech_docs_cli %} checked {% endif
                                %} />
                            <label class="pf-v5-c-check__label" for="tech_docs_cli_{{ alias.alias_id }}">{{
                                form.tech_docs_cli.label }}</label>
                        </div>
                    </div>
                </div>
            </div>
            <button type="button" class="pf-v5-c-button pf-m-danger remove-alias-group"
                style="display: none;">Delete</button>
        </div>
        {% endfor %}
    </div>
    <div id="new-aliases">
        <!-- Template for New Alias Group -->
        {% for alias in existing_aliases %}
        <div class="product-alias-group template" "pf-v5-c-form__group" style="display:none;">
    
            <div class="pf-v5-l-grid pf-m-gutter">
                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_name_PLACEHOLDER">{{ form.alias_name.label }}">
                        </label>
                        <input type="text" name="alias_name_PLACEHOLDER" id="alias_name_PLACEHOLDER" cols="30"
                            class="pf-v5-c-form-control" />
                    </div>
    
                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_notes_PLACEHOLDER">{{ form.alias_notes.label }}">
                        </label>
                        <textarea name="alias_notes_PLACEHOLDER" id="alias_notes_PLACEHOLDER" cols="30"
                            class="pf-v5-c-form-control"> </textarea>
                    </div>
                </div>
    
                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <div class="pf-v5-c-form__group">
                        <label class="pf-v5-c-form__label" for="alias_type_PLACEHOLDER">{{ form.alias_type.label }}</label>
                        <select class="pf-v5-c-form-control" name="alias_type_PLACEHOLDER" id="alias_type_PLACEHOLDER">
                            {% for value, label in form.alias_type.choices %}
                            <option value="{{ value }}">{{ label }}</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>
    
                <div class="pf-v5-l-grid__item pf-m-12-col pf-m-6-col-on-sm pf-m-4-col-on-md">
                    <label class="pf-v5-c-form__label" for="{{ form.alias_type.id }}">
                        <span class="pf-v5-c-form__label-text">Is?</span>
                    </label>
                    <div class="pf-v5-c-form__group">
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="alias_approved_PLACEHOLDER"
                                id="alias_approved_PLACEHOLDER" />
                            <label class="pf-v5-c-check__label" for="alias_approved_PLACEHOLDER">{{
                                form.alias_approved.label }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="previous_name_PLACEHOLDER"
                                id="previous_name_PLACEHOLDER" />
                            <label class="pf-v5-c-check__label" for="previous_name_PLACEHOLDER">{{ form.previous_name.label
                                }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_PLACEHOLDER"
                                id="tech_docs_PLACEHOLDER" />
                            <label class="pf-v5-c-check__label" for="tech_docs_PLACEHOLDER">{{ form.tech_docs.label
                                }}</label>
                        </div>
                        <div class="pf-v5-c-check">
                            <input type="checkbox" class="pf-v5-c-check__input" name="tech_docs_cli_PLACEHOLDER"
                                id="tech_docs_cli_PLACEHOLDER" />
                            <label class="pf-v5-c-check__label" for="tech_docs_cli_PLACEHOLDER">{{ form.tech_docs_cli.label
                                }}</label>
                        </div>
                    </div>
                </div>
            </div>
            <button type="button" class="pf-v5-c-button pf-m-danger remove-alias-group"
                style="display: none;">Delete</button>
        </div>
    </div>
    <button type="button" class="pf-v5-c-button pf-m-primary add-alias-group">Add more
        aliases</button>
</fieldset>

File "/home/gtrivedi/git/gitlab/opl-ui/templates/opl/edit.html", line 469, in template
    {% endif %}
jinja2.exceptions.TemplateSyntaxError: Encountered unknown tag 'endif'. You probably made a nesting mistake. Jinja is expecting this tag, but currently looking for 'endfor' or 'else'. The innermost block that needs to be closed is 'for'.
