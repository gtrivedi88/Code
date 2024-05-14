{% if product_aliases %}
    <fieldset class="product-alias-section">
        <legend>Product alias information</legend>
        <p><b>Note:</b> Always use full product name on first use and whenever clarity is needed. After first use, you may use approved short
        forms or acronyms. Tech Docs (Technical, customer-facing documentation) refers to non-marketing, non-sales content used
        to train customers, assist with installation, etc., such as getting started guides, Jira/Bugzilla entries, and support
        case summaries.</p>
        <br>
        <div class="alias-table">
            <!-- Table Headers -->
            <div class="alias-table-header">
                <div class="alias-table-cell"><strong>Alias name</strong></div>
                <div class="alias-table-cell"><strong>Approved for general use</strong></div>
                <div class="alias-table-cell"><strong>Previous name</strong></div>
                <div class="alias-table-cell"><strong>Approved for tech docs</strong></div>
                <div class="alias-table-cell"><strong>Approved for tech docs code/cli</strong></div>
                <div class="alias-table-cell"><strong>Alias notes</strong></div>
            </div>
            <!-- Each Row Represents a Set of Alias Information -->
            {% for alias in product_aliases %}
            <div class="alias-table-row">
                <div class="alias-table-cell">{{ alias.alias_name }}</div>
                <div class="alias-table-cell">
                    {% if alias.alias_approved %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.previous_name %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.tech_docs %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">
                    {% if alias.tech_docs_cli %}
                    <strong>Yes</strong>
                    {% else %}
                    No
                    {% endif %}
                </div>
                <div class="alias-table-cell">{{ alias.alias_notes or "N/A" }}</div>
            </div>
            {% endfor %}
        </div>
    </fieldset>
    {% endif %}

/* Alias table css */

.alias-table {
    display: block;
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    white-space: wrap;
    
}

.alias-table-header,
.alias-table-row {
    display: table;
    width: 100%;
    table-layout: fixed;
    
}

.alias-table-cell {
    display: table-cell;
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
    word-wrap: break-word !important;
    hyphens: auto;
    
}

.alias-table-header .alias-table-cell,
.alias-table-row .alias-table-cell:first-child {
    font-weight: bold;
    background-color: #f2f2f2;
    
}

.alias-table-row:nth-child(odd) {
    background-color: #f9f9f9;
}

.alias-table-row:hover {
    background-color: #eaeaea;
}

.parent-columns,
.notes-columns {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
