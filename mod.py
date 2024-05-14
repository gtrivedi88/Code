<div class="tile-container">
    <!-- View Product Card -->
    <div class="card">
        <img src="{{ url_for('static', filename='/images/view_product.png') }}" class="card-img-top" alt="View Product">
        <div class="card-body">
            <h4 class="card-title">View Product</h4>
            <p class="card-text">Explore the list of products.</p>
            <a href="opl/search-to-view-products" class="btn">View</a>
        </div>
    </div>

    {% if "/opl-editor" in needs.group %}
    <!-- Edit Product Card -->
    <div class="card">
        <img src="{{ url_for('static', filename='/images/edit_product.png') }}" class="card-img-top" alt="Edit Product">
        <div class="card-body">
            <h4 class="card-title">Edit Product</h4>
            <p class="card-text">Modify existing product details.</p>
            <a href="opl/search-to-edit-products" class="btn">Edit</a>
        </div>
    </div>
    {% endif %}

    {% if "/opl-editor" in needs.group %}
    <!-- Add Product Card -->
    <div class="card">
        <img src="{{ url_for('static', filename='/images/add_product.png') }}" class="card-img-top" alt="Add Product">
        <div class="card-body">
            <h4 class="card-title">Add Product</h4>
            <p class="card-text">Introduce a new product to the list.</p>
            <a href="opl/add-product" class="btn">Add</a>
        </div>
    </div>
    {% endif %}
</div>
