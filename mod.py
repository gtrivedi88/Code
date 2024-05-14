<!-- Product Release Information -->

    {% if product_mkt_life.product_release or product_mkt_life.product_release_detail or
    product_mkt_life.product_release_link %}
    <fieldset class="product-release-info">
        <legend>Product release information</legend>
        {% if product_mkt_life.product_release %}
        <div class="field-pair">
            <label>Release date</label>
            <span>{{ product_mkt_life.product_release.strftime('%m-%d-%Y') }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_release_detail %}
        <div class="field-pair">
            <label>Release detail</label>
            <span>{{ product_mkt_life.product_release_detail }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_release_link %}
        <div class="field-pair">
            <label>Release reference</label>
            <span><a href="{{ product_mkt_life.product_release_link }}" target="_blank">{{ product_mkt_life.product_release_link }}</a></span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}

    <!-- Product EOL Information -->

    {% if product_mkt_life.product_eol or product_mkt_life.product_eol_detail or product_mkt_life.product_eol_link %}
    <fieldset class="product-eol-info">
        <legend>Product end of life information</legend>
        {% if product_mkt_life.product_eol %}
        <div class="field-pair">
            <label>Product end of life (EOL) date</label>
            <span>{{ product_mkt_life.product_eol.strftime('%m-%d-%Y') }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_eol_detail %}
        <div class="field-pair">
            <label>Product end of life (EOL) details</label>
            <span>{{ product_mkt_life.product_eol_detail }}</span>
        </div>
        {% endif %}

        {% if product_mkt_life.product_eol_link %}
        <div class="field-pair">
            <label>Product end of life (EOL) reference</label>
            <span><a href="{{ product_mkt_life.product_eol_link }}" target="_blank">{{ product_mkt_life.product_eol_link }}</a></span>
        </div>
        {% endif %}
    </fieldset>
    {% endif %}
