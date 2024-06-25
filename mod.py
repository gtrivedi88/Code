<header class="pf-v5-c-masthead">
  <div class="pf-v5-c-masthead__main pf-v5-l-flex pf-m-align-items-center">
    <div class="pf-v5-c-masthead__brand pf-v5-l-flex pf-m-align-items-center">
      <a href="{{ url_for('home') }}" style="display: flex; align-items: center;">
        <img src="{{ url_for('static', filename='images/red-hat-logo.png') }}" alt="Red Hat Logo" />
        <div style="border-left: 1px solid white; height: 40px;"></div>
      
      <div class="custom-heading" style="margin: 0 10px;">
        <h1 class="pf-v5-c-title pf-m-md" style="margin: 0;">Red Hat</h1>
        <h2 class="pf-v5-c-title pf-m-sm" style="margin: 0; font-weight: bold;">Official Product List</h2>
      </div>
      </a>
    </div>
  </div>
  <div class="pf-v5-c-masthead__content">
    <div class="pf-v5-c-toolbar pf-m-full-height pf-m-static" id="masthead-advanced-with-menu-example-masthead-toolbar">
      <div class="pf-v5-c-toolbar__content">
        <div class="pf-v5-c-toolbar__content-section">
          <div
            class="pf-v5-c-toolbar__group pf-m-icon-button-group pf-m-align-right pf-m-spacer-none pf-m-spacer-md-on-md">
            <input type="text" placeholder="Search products" class="pf-v5-c-form-control" />
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
