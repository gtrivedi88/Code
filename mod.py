<header class="pf-v5-c-masthead">
  <div class="pf-v5-c-masthead__main pf-v5-l-flex pf-m-align-items-center">
    <div class="pf-v5-c-masthead__brand pf-v5-l-flex pf-m-align-items-center">
      <a href="{{ url_for('home') }}" style="display: flex; align-items: center; text-decoration: none;">
        <img src="{{ url_for('static', filename='images/red-hat-logo.png') }}" alt="Red Hat Logo" />
        <div style="border-left: 1px solid white; height: 40px;"></div>
        <div class="custom-heading" style="margin-left: 15px;">
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
            class="pf-v5-c-toolbar__group pf-m-icon-button-group pf-m-align-right pf-m-spacer-none pf-m-spacer-md-on-md"
            style="position: relative;">
            <button class="search-icon" id="search-button" onclick="toggleSearchBar()">
              <img src="{{ url_for('static', filename='images/search.svg') }}" alt="Search Icon" />
            </button>
            <div class="search-bar-container pf-v5-c-search-input" id="search-bar">
              <div class="pf-v5-c-input-group">
                <div class="pf-v5-c-search-input__bar">
                  <span class="pf-v5-c-search-input__text">
                    <span class="pf-v5-c-search-input__icon">
                      <i class="fas fa-search fa-fw" aria-hidden="true"></i>
                    </span>
                    <input class="pf-v5-c-search-input__text-input" type="text" placeholder="Find by name"
                      aria-label="Find by name" id="search-input" />
                  </span>
                </div>
                <button class="pf-v5-c-button pf-m-control" type="submit" aria-label="Search" onclick="submitSearch()">
                  <i class="fas fa-arrow-right" aria-hidden="true"></i>
                </button>
              </div>
            </div>
            <button class="close-icon" id="close-button" onclick="toggleSearchBar()">×</button>
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
  
  <style>
    .search-bar-container {
      display: none;
      align-items: center;
      background-color: var(--Secondary---pf-v5-global--secondary-color--100, #6A6E73);
      border: 1px solid #ccc;
      border-radius: 0;
      padding: 6px 8px;
      position: relative;
      width: 469px;
      min-height: 36px;
      max-height: 36px;
      align-items: center;
      gap: 4px;
      box-shadow: 0px -1px 0px 0px #8A8D90 inset, 1px 0px 0px 0px #F0F0F0 inset, 0px 1px 0px 0px #F0F0F0 inset, -1px 0px 0px 0px #F0F0F0 inset;
    }
  
    .search-bar-container.active {
      display: flex;
    }
  
    .pf-v5-c-search-input__icon i {
      color: var(--pf-global--icon--Color--dark--light, #FFFFFF);
    }
  
    .pf-v5-c-search-input__text-input {
      background: none;
      border: none;
      outline: none;
      color: var(--pf-global--Color--light-100, #FFFFFF);
      width: 100%;
      padding-left: 8px;
    }
  
    .pf-v5-c-button.pf-m-control {
      background: none;
      border: none;
      color: var(--pf-global--Color--light-100, #FFFFFF);
    }
  
    .close-icon {
      display: none;
      background: none;
      border: none;
      font-size: 16px;
      margin-left: 8px;
      cursor: pointer;
      color: var(--pf-global--Color--light-100, #FFFFFF);
    }
  
    .close-icon.active {
      display: block;
    }
  
    .search-icon {
      background: none;
      border: none;
      cursor: pointer;
    }
  
    .search-results {
      position: absolute;
      top: 100%;
      left: 0;
      background: white;
      border: 1px solid #ccc;
      border-top: none;
      list-style: none;
      margin: 0;
      padding: 0;
      width: 100%;
      max-height: 200px;
      overflow-y: auto;
      z-index: 1000;
      display: none;
    }
  
    .search-results li {
      padding: 8px;
      cursor: pointer;
      color: black;
      border-bottom: 1px solid #ddd;
    }
  
    .search-results li:hover {
      background: #f0f0f0;
    }
  </style>
  
  <script>
    function toggleSearchBar() {
      const searchBar = document.getElementById('search-bar');
      const searchButton = document.getElementById('search-button');
      const closeButton = document.getElementById('close-button');
      const searchResults = document.getElementById('search-results');

      if (searchBar.classList.contains('active')) {
        searchBar.classList.remove('active');
        closeButton.classList.remove('active');
        searchButton.style.display = 'block';
        searchResults.style.display = 'none';
      } else {
        searchBar.classList.add('active');
        closeButton.classList.add('active');
        searchButton.style.display = 'none';
      }
    }

    function submitSearch() {
      const query = document.getElementById('search-input').value;
      if (query.length > 0) {
        window.location.href = `/opl/search-to-view-products?product_name=${encodeURIComponent(query)}`;
      }
    }

    document.getElementById('search-input').addEventListener('input', function () {
      const query = this.value;
      const searchResults = document.getElementById('search-results');

      if (query.length < 2) {
        searchResults.style.display = 'none';
        return;
      }

      fetch(`/opl/ajax-search?q=${query}`)
        .then(response => response.json())
        .then(data => {
          searchResults.innerHTML = '';
          if (data.length > 0) {
            searchResults.style.display = 'block';
            data.forEach(product => {
              const li = document.createElement('li');
              li.textContent = product.name;
              li.addEventListener('click', function () {
                window.location.href = `/opl/product/${product.id}`;
              });
              searchResults.appendChild(li);
            });
          } else {
            searchResults.style.display = 'none';
          }
        });
    });
  </script>
