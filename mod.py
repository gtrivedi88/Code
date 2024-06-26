<header class="pf-v5-c-masthead">
  <div class="pf-v5-c-masthead__main pf-v5-l-flex pf-m-align-items-center">
    <div class="pf-v5-c-masthead__brand pf-v5-l-flex pf-m-align-items-center">
      <a href="{{ url_for('home') }}" style="display: flex; align-items: center; text-decoration: none;">
        <img src="{{ url_for('static', filename='images/red-hat-logo.svg') }}" alt="Red Hat Logo" />        
      </a>
    </div>
  </div>
  <div class="pf-v5-c-masthead__content">
    <div class="pf-v5-c-toolbar pf-m-full-height pf-m-static" id="masthead-advanced-with-menu-example-masthead-toolbar">
      <div class="pf-v5-c-toolbar__content">
        <div class="pf-v5-c-toolbar__content-section">
          <div
            class="pf-v5-c-toolbar__group pf-m-icon-button-group pf-m-align-right pf-m-spacer-none pf-m-spacer-md-on-md"
            style="position: relative;">
            <div class="search-bar-container pf-v5-c-search-input" id="search-bar">
              <div class="pf-v5-c-input-group">
                <span class="pf-v5-c-search-input__icon">
                  <i class="fas fa-search fa-fw" aria-hidden="true"></i>
                </span>
                <input class="pf-v5-c-search-input__text-input" type="text" placeholder="Search products"
                  aria-label="Search products" id="search-input" />
              </div>
            </div>
            <button class="pf-v5-c-button pf-m-control search-arrow" type="submit" aria-label="Search"
              onclick="submitSearch()">
              <i class="fas fa-arrow-right" aria-hidden="true"></i>
            </button>
            <ul class="search-results" id="search-results"></ul>
          </div>
          <div class="pf-v5-c-toolbar__item pf-m-hidden pf-m-visible-on-sm">
            {% if "anonymous" in needs.type %}
            <a class="pf-v5-c-button pf-m-primary pf-m-small" href="/saml/sso">
              <span class="pf-v5-c-menu-toggle__text">Login</span>
            </a>
            {% elif "authenticated" in needs.type %}
            <span class="pf-v5-c-menu-toggle__text">Welcome, {{ user }}!</span>&nbsp;&nbsp;&nbsp;
            <a class="pf-v5-c-button pf-m-primary pf-m-small" href="/saml/logout">
              <span class="pf-v5-c-menu-toggle__text">Logout</span>
            </a>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  </div>
</header>

<script src="{{ url_for('static', filename='scripts/search.js') }}"></script>
