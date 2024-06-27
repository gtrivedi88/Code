<!doctype html>
{% include 'head.html' %}
<body>
  <!doctype html>
  {% include 'head.html' %}
  
  <body>
    <div class="pf-v5-c-page" id="primary-detail-expanded-example">
      <div class="pf-v5-c-skip-to-content">
        <a class="pf-v5-c-button pf-m-primary" href="#main-content-primary-detail-expanded-example">Skip to
          content</a>
      </div>
      <header class="pf-v5-c-masthead pf-m-display-stack pf-m-display-inline-on-lg"
        id="primary-detail-expanded-example-masthead">
        <span class="pf-v5-c-masthead__toggle">
          <button class="pf-v5-c-button pf-m-plain" type="button" aria-label="Global navigation">
            <i class="fas fa-bars" aria-hidden="true"></i>
          </button>
        </span>
        <div class="pf-v5-c-masthead__main">
          <a class="pf-v5-c-masthead__brand" href="#">
            <img class="pf-v5-c-brand" src="{{ url_for('static', filename='images/red-hat-logo.svg') }}" alt="Red Hat logo"
              style="--pf-v5-c-brand--Height:36px" />
          </a>
        </div>
        <div class="pf-v5-c-masthead__content">
          <div class="pf-v5-c-toolbar pf-m-full-height pf-m-static" id="primary-detail-expanded-example-masthead-toolbar">
            <div class="pf-v5-c-toolbar__content">
              <div class="pf-v5-c-toolbar__content-section">
                <div
                  class="pf-v5-c-toolbar__group pf-m-icon-button-group pf-m-align-right pf-m-spacer-none pf-m-spacer-md-on-md">
                  <div class="pf-v5-c-toolbar__group pf-m-icon-button-group pf-m-hidden pf-m-visible-on-lg">

                    




                    <div class="pf-v5-c-toolbar__item">
                      <button class="pf-v5-c-menu-toggle pf-m-plain" type="button" aria-expanded="false"
                        aria-label="Application launcher">
                        <i class="fas fa-th" aria-hidden="true"></i>
                      </button>
                    </div>
                    <div class="pf-v5-c-toolbar__item">
                      <button class="pf-v5-c-menu-toggle pf-m-plain" type="button" aria-expanded="false"
                        aria-label="Settings">
                        <i class="fas fa-cog" aria-hidden="true"></i>
                      </button>
                    </div>
                    <div class="pf-v5-c-toolbar__item">
                      <button class="pf-v5-c-menu-toggle pf-m-plain" type="button" aria-expanded="false"
                        aria-label="Help">
                        <i class="fas fa-question-circle" aria-hidden="true"></i>
                      </button>
                    </div>
                  </div>
                  <div class="pf-v5-c-toolbar__item pf-m-hidden-on-lg">
                    <button class="pf-v5-c-menu-toggle pf-m-plain" type="button" aria-expanded="false"
                      aria-label="Actions">
                      <i class="fas fa-ellipsis-v" aria-hidden="true"></i>
                    </button>
                  </div>
                </div>
                <div class="pf-v5-c-toolbar__item pf-m-hidden pf-m-visible-on-sm">
                  <button class="pf-v5-c-menu-toggle pf-m-full-height" type="button" aria-expanded="false">
                    <span class="pf-v5-c-menu-toggle__icon">
                      <img class="pf-v5-c-avatar" alt="Avatar image" src="/assets/images/img_avatar-light.svg" />
                    </span>
                    <span class="pf-v5-c-menu-toggle__text">Ned Username</span>
                    <span class="pf-v5-c-menu-toggle__controls">
                      <span class="pf-v5-c-menu-toggle__toggle-icon">
                        <i class="fas fa-caret-down" aria-hidden="true"></i>
                      </span>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      <div class="pf-v5-c-page__sidebar">
        <div class="pf-v5-c-page__sidebar-body">
          <nav class="pf-v5-c-nav" id="primary-detail-expanded-example-primary-nav" aria-label="Global">
            <ul class="pf-v5-c-nav__list" role="list">
              <li class="pf-v5-c-nav__item">
                <a href="#" class="pf-v5-c-nav__link">System panel</a>
              </li>
              <li class="pf-v5-c-nav__item">
                <a href="#" class="pf-v5-c-nav__link pf-m-current" aria-current="page">Policy</a>
              </li>
              <li class="pf-v5-c-nav__item">
                <a href="#" class="pf-v5-c-nav__link">Authentication</a>
              </li>
              <li class="pf-v5-c-nav__item">
                <a href="#" class="pf-v5-c-nav__link">Network services</a>
              </li>
              <li class="pf-v5-c-nav__item">
                <a href="#" class="pf-v5-c-nav__link">Server</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <main class="pf-v5-c-page__main" tabindex="-1" id="main-content-primary-detail-expanded-example">
        <section class="pf-v5-c-page__main-breadcrumb pf-m-limit-width">
          <div class="pf-v5-c-page__main-body">
            <nav class="pf-v5-c-breadcrumb" aria-label="breadcrumb">
              <ol class="pf-v5-c-breadcrumb__list" role="list">
                <li class="pf-v5-c-breadcrumb__item">
                  <a href="#" class="pf-v5-c-breadcrumb__link">Section home</a>
                </li>
                <li class="pf-v5-c-breadcrumb__item">
                  <span class="pf-v5-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
  
                  <a href="#" class="pf-v5-c-breadcrumb__link">Section title</a>
                </li>
                <li class="pf-v5-c-breadcrumb__item">
                  <span class="pf-v5-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
  
                  <a href="#" class="pf-v5-c-breadcrumb__link">Section title</a>
                </li>
                <li class="pf-v5-c-breadcrumb__item">
                  <span class="pf-v5-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
  
                  <a href="#" class="pf-v5-c-breadcrumb__link pf-m-current" aria-current="page">Section
                    landing</a>
                </li>
              </ol>
            </nav>
          </div>
        </section>
        <section class="pf-v5-c-page__main-section pf-m-limit-width pf-m-light">
          <div class="pf-v5-c-page__main-body">
            <div class="pf-v5-c-content">
              <h1>Main title</h1>
              <p>This is a full page demo.</p>
            </div>
          </div>
        </section>
        <div class="pf-v5-c-divider" role="separator"></div>
        <section class="pf-v5-c-page__main-section pf-m-no-padding">
          <!-- Drawer -->
          <div class="pf-v5-c-drawer pf-m-expanded pf-m-inline-on-2xl">
            <div class="pf-v5-c-drawer__main">
              <!-- Content -->
              <div class="pf-v5-c-drawer__content">
                <div class="pf-v5-c-drawer__body">
                  <div class="pf-v5-c-toolbar pf-m-page-insets" id="primary-detail-expanded-example-drawer-toolbar">
                    <div class="pf-v5-c-toolbar__content">
                      <div class="pf-v5-c-toolbar__content-section pf-m-nowrap">
                        <div class="pf-v5-c-toolbar__group pf-m-toggle-group pf-m-show-on-xl">
                          <div class="pf-v5-c-toolbar__toggle">
                            <button class="pf-v5-c-menu-toggle pf-m-plain" type="button" aria-expanded="false"
                              aria-label="Show filters"
                              aria-controls="primary-detail-expanded-example-drawer-toolbar-expandable-content">
                              <i class="fas fa-filter" aria-hidden="true"></i>
                            </button>
                          </div>
  
                          <div class="pf-v5-c-toolbar__item pf-m-search-filter">
                            <div class="pf-v5-c-input-group" aria-label="search filter" role="group">
                              <div class="pf-v5-c-input-group__item">
                                <button class="pf-v5-c-menu-toggle" type="button" aria-expanded="false"
                                  id="primary-detail-expanded-example-drawer-toolbar-search-filter-menu">
                                  <span class="pf-v5-c-menu-toggle__icon">
                                    <i class="fas fa-filter" aria-hidden="true"></i>
                                  </span>
                                  <span class="pf-v5-c-menu-toggle__text">Name</span>
                                  <span class="pf-v5-c-menu-toggle__controls">
                                    <span class="pf-v5-c-menu-toggle__toggle-icon">
                                      <i class="fas fa-caret-down" aria-hidden="true"></i>
                                    </span>
                                  </span>
                                </button>
                              </div>
                              <div class="pf-v5-c-input-group__item pf-m-fill">
                                <div class="pf-v5-c-text-input-group">
                                  <div class="pf-v5-c-text-input-group__main pf-m-icon">
                                    <span class="pf-v5-c-text-input-group__text">
                                      <span class="pf-v5-c-text-input-group__icon">
                                        <i class="fas fa-fw fa-search"></i>
                                      </span>
                                      <input class="pf-v5-c-text-input-group__text-input" type="text"
                                        placeholder="Filter by name" value aria-label="Search input" />
                                    </span>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
  
                          <div class="pf-v5-c-toolbar__group pf-m-filter-group">
                            <div class="pf-v5-c-toolbar__item">
                              <div class="pf-v5-c-select">
                                <span id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-label"
                                  hidden>Choose many</span>
  
                                <button class="pf-v5-c-select__toggle" type="button"
                                  id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-toggle"
                                  aria-haspopup="true" aria-expanded="false"
                                  aria-labelledby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-label primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-toggle">
                                  <div class="pf-v5-c-select__toggle-wrapper">
                                    <span class="pf-v5-c-select__toggle-text">Status</span>
                                  </div>
                                  <span class="pf-v5-c-select__toggle-arrow">
                                    <i class="fas fa-caret-down" aria-hidden="true"></i>
                                  </span>
                                </button>
  
                                <div class="pf-v5-c-select__menu" hidden>
                                  <fieldset class="pf-v5-c-select__menu-fieldset" aria-label="Select input">
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item pf-m-description"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        aria-describedby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active-description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active-input" />
                                      <span class="pf-v5-c-check__label">Active</span>
                                      <span class="pf-v5-c-check__description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-active-description">This
                                        is a description</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item pf-m-description"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        aria-describedby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled-description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled-input" />
                                      <span class="pf-v5-c-check__label">Canceled</span>
                                      <span class="pf-v5-c-check__description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-canceled-description">This
                                        is a really long description that describes
                                        the
                                        menu item. This is a really long description
                                        that describes the menu item.</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-paused"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-paused-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-paused-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-paused-input" />
                                      <span class="pf-v5-c-check__label">Paused</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-warning"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-warning-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-warning-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-warning-input" />
                                      <span class="pf-v5-c-check__label">Warning</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-restarted"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-restarted-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-restarted-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-status-restarted-input" />
                                      <span class="pf-v5-c-check__label">Restarted</span>
                                    </label>
                                  </fieldset>
                                </div>
                              </div>
                            </div>
                            <div class="pf-v5-c-toolbar__item">
                              <div class="pf-v5-c-select">
                                <span id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-label"
                                  hidden>Choose many</span>
  
                                <button class="pf-v5-c-select__toggle" type="button"
                                  id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-toggle"
                                  aria-haspopup="true" aria-expanded="false"
                                  aria-labelledby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-label primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-toggle">
                                  <div class="pf-v5-c-select__toggle-wrapper">
                                    <span class="pf-v5-c-select__toggle-text">Risk</span>
                                  </div>
                                  <span class="pf-v5-c-select__toggle-arrow">
                                    <i class="fas fa-caret-down" aria-hidden="true"></i>
                                  </span>
                                </button>
  
                                <div class="pf-v5-c-select__menu" hidden>
                                  <fieldset class="pf-v5-c-select__menu-fieldset" aria-label="Select input">
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item pf-m-description"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        aria-describedby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active-description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active-input" />
                                      <span class="pf-v5-c-check__label">Active</span>
                                      <span class="pf-v5-c-check__description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-active-description">This
                                        is a description</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item pf-m-description"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        aria-describedby="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled-description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled-input" />
                                      <span class="pf-v5-c-check__label">Canceled</span>
                                      <span class="pf-v5-c-check__description"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-canceled-description">This
                                        is a really long description that describes
                                        the
                                        menu item. This is a really long description
                                        that describes the menu item.</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-paused"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-paused-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-paused-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-paused-input" />
                                      <span class="pf-v5-c-check__label">Paused</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-warning"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-warning-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-warning-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-warning-input" />
                                      <span class="pf-v5-c-check__label">Warning</span>
                                    </label>
                                    <label class="pf-v5-c-check pf-v5-c-select__menu-item"
                                      id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-restarted"
                                      for="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-restarted-input">
                                      <input class="pf-v5-c-check__input" type="checkbox"
                                        id="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-restarted-input"
                                        name="primary-detail-expanded-example-drawer-toolbar-select-checkbox-risk-restarted-input" />
                                      <span class="pf-v5-c-check__label">Restarted</span>
                                    </label>
                                  </fieldset>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
  
                        <div class="pf-v5-c-toolbar__item">
                          <button class="pf-v5-c-button pf-m-plain" type="button" aria-label="Sort">
                            <i class="fas fa-sort-amount-down pf-v5-m-mirror-inline-rtl" aria-hidden="true"></i>
                          </button>
                        </div>
  
                        <div class="pf-v5-c-overflow-menu"
                          id="primary-detail-expanded-example-drawer-toolbar-overflow-menu">
                          <div class="pf-v5-c-overflow-menu__content pf-v5-u-display-none pf-v5-u-display-flex-on-lg">
                            <div class="pf-v5-c-overflow-menu__group pf-m-button-group">
                              <div class="pf-v5-c-overflow-menu__item">
                                <button class="pf-v5-c-button pf-m-primary" type="button">Create
                                  instance</button>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v5-c-overflow-menu__control">
                            <div class="pf-v5-c-dropdown">
                              <button class="pf-v5-c-button pf-v5-c-dropdown__toggle pf-m-plain" type="button"
                                id="primary-detail-expanded-example-drawer-toolbar-overflow-menu-dropdown-toggle"
                                aria-label="Dropdown with additional options" aria-expanded="false">
                                <i class="fas fa-ellipsis-v" aria-hidden="true"></i>
                              </button>
                              <ul class="pf-v5-c-dropdown__menu" role="menu"
                                aria-labelledby="primary-detail-expanded-example-drawer-toolbar-overflow-menu-dropdown-toggle"
                                hidden>
                                <li role="none">
                                  <button role="menuitem" class="pf-v5-c-dropdown__menu-item">Action
                                    7</button>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </div>
  
                        <div class="pf-v5-c-toolbar__item pf-m-pagination">
                          <div class="pf-v5-c-pagination pf-m-compact">
                            <button class="pf-v5-c-menu-toggle pf-m-plain pf-m-text" type="button" aria-expanded="false"
                              id="primary-detail-expanded-example-drawer-toolbar-top-pagination">
                              <span class="pf-v5-c-menu-toggle__text">
                                <b>1 - 10</b>&nbsp;of&nbsp;
                                <b>36</b>
                              </span>
                              <span class="pf-v5-c-menu-toggle__controls">
                                <span class="pf-v5-c-menu-toggle__toggle-icon">
                                  <i class="fas fa-caret-down" aria-hidden="true"></i>
                                </span>
                              </span>
                            </button>
                            <nav class="pf-v5-c-pagination__nav" aria-label="Toolbar top pagination">
                              <div class="pf-v5-c-pagination__nav-control pf-m-prev">
                                <button class="pf-v5-c-button pf-m-plain" type="button" disabled
                                  aria-label="Go to previous page">
                                  <i class="fas fa-angle-left" aria-hidden="true"></i>
                                </button>
                              </div>
                              <div class="pf-v5-c-pagination__nav-control pf-m-next">
                                <button class="pf-v5-c-button pf-m-plain" type="button" aria-label="Go to next page">
                                  <i class="fas fa-angle-right" aria-hidden="true"></i>
                                </button>
                              </div>
                            </nav>
                          </div>
                        </div>
                      </div>
  
                      <div class="pf-v5-c-toolbar__expandable-content pf-m-hidden"
                        id="primary-detail-expanded-example-drawer-toolbar-expandable-content" hidden>
                      </div>
                    </div>
                  </div>
                  <ul class="pf-v5-c-data-list" role="list" aria-label="Simple data list example"
                    id="primary-detail-expanded-example-data-list">
                    <li class="pf-v5-c-data-list__item"
                      aria-labelledby="primary-detail-expanded-example-data-list-item-1">
                      <div class="pf-v5-c-data-list__item-row">
                        <div class="pf-v5-c-data-list__item-content">
                          <div class="pf-v5-c-data-list__cell pf-m-align-left">
                            <div class="pf-v5-l-flex pf-m-column pf-m-space-items-md">
                              <div class="pf-v5-l-flex pf-m-column pf-m-space-items-none">
                                <div class="pf-v5-l-flex__item">
                                  <p id="primary-detail-expanded-example-data-list-item-1">
                                    patternfly</p>
                                </div>
                                <div class="pf-v5-l-flex__item">
                                  <small>
                                    Working repo for PatternFly 4
                                    <a href>https://pf4.patternfly.org/</a>
                                  </small>
                                </div>
                              </div>
                              <div class="pf-v5-l-flex pf-m-wrap">
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code-branch" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>10</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>4</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-cube" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>5</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex__item">Updated 2 days ago</div>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v5-c-data-list__cell pf-m-align-right pf-m-no-fill">
                            <button class="pf-v5-c-button pf-m-secondary" type="button">Action</button>
                            <button class="pf-v5-c-button pf-m-link" type="button">Link</button>
                          </div>
                        </div>
                      </div>
                    </li>
  
                    <li class="pf-v5-c-data-list__item"
                      aria-labelledby="primary-detail-expanded-example-data-list-item-2">
                      <div class="pf-v5-c-data-list__item-row">
                        <div class="pf-v5-c-data-list__item-content">
                          <div class="pf-v5-c-data-list__cell pf-m-align-left">
                            <div class="pf-v5-l-flex pf-m-column pf-m-space-items-md">
                              <div class="pf-v5-l-flex pf-m-column pf-m-space-items-none">
                                <div class="pf-v5-l-flex__item">
                                  <p id="primary-detail-expanded-example-data-list-item-2">
                                    patternfly-elements</p>
                                </div>
                                <div class="pf-v5-l-flex__item">
                                  <small>PatternFly elements</small>
                                </div>
                              </div>
                              <div class="pf-v5-l-flex pf-m-wrap">
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code-branch" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>5</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>9</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-cube" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>2</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-check-circle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>11</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-exclamation-triangle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>4</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-times-circle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>1</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex__item">Updated 2 days ago</div>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v5-c-data-list__cell pf-m-align-right pf-m-no-fill">
                            <button class="pf-v5-c-button pf-m-secondary" type="button">Action</button>
                            <button class="pf-v5-c-button pf-m-link" type="button">Link</button>
                          </div>
                        </div>
                      </div>
                    </li>
  
                    <li class="pf-v5-c-data-list__item"
                      aria-labelledby="primary-detail-expanded-example-data-list-item-3">
                      <div class="pf-v5-c-data-list__item-row">
                        <div class="pf-v5-c-data-list__item-content">
                          <div class="pf-v5-c-data-list__cell pf-m-align-left">
                            <p id="primary-detail-expanded-example-data-list-item-3">
                              patternfly-unified-design-kit</p>
                          </div>
                          <div class="pf-v5-c-data-list__cell pf-m-align-right pf-m-no-fill">
                            <button class="pf-v5-c-button pf-m-secondary" type="button">Action</button>
                            <button class="pf-v5-c-button pf-m-link" type="button">Link</button>
                          </div>
                        </div>
                      </div>
                    </li>
  
                    <li class="pf-v5-c-data-list__item"
                      aria-labelledby="primary-detail-expanded-example-data-list-item-4">
                      <div class="pf-v5-c-data-list__item-row">
                        <div class="pf-v5-c-data-list__item-content">
                          <div class="pf-v5-c-data-list__cell pf-m-align-left">
                            <div class="pf-v5-l-flex pf-m-column pf-m-space-items-md">
                              <div class="pf-v5-l-flex pf-m-column pf-m-space-items-none">
                                <div class="pf-v5-l-flex__item">
                                  <p id="primary-detail-expanded-example-data-list-item-4">
                                    patternfly</p>
                                </div>
                                <div class="pf-v5-l-flex__item">
                                  <small>
                                    Working repo for PatternFly 4
                                    <a href>https://pf4.patternfly.org/</a>
                                  </small>
                                </div>
                              </div>
                              <div class="pf-v5-l-flex pf-m-wrap">
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code-branch" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>10</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>4</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-cube" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>5</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex__item">Updated 2 days ago</div>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v5-c-data-list__cell pf-m-align-right pf-m-no-fill">
                            <button class="pf-v5-c-button pf-m-secondary" type="button">Action</button>
                            <button class="pf-v5-c-button pf-m-link" type="button">Link</button>
                          </div>
                        </div>
                      </div>
                    </li>
  
                    <li class="pf-v5-c-data-list__item"
                      aria-labelledby="primary-detail-expanded-example-data-list-item-5">
                      <div class="pf-v5-c-data-list__item-row">
                        <div class="pf-v5-c-data-list__item-content">
                          <div class="pf-v5-c-data-list__cell pf-m-align-left">
                            <div class="pf-v5-l-flex pf-m-column pf-m-space-items-md">
                              <div class="pf-v5-l-flex pf-m-column pf-m-space-items-none">
                                <div class="pf-v5-l-flex__item">
                                  <p id="primary-detail-expanded-example-data-list-item-5">
                                    patternfly-elements</p>
                                </div>
                                <div class="pf-v5-l-flex__item">
                                  <small>PatternFly elements</small>
                                </div>
                              </div>
                              <div class="pf-v5-l-flex pf-m-wrap">
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code-branch" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>5</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-code" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>9</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-cube" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>2</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-check-circle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>11</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-exclamation-triangle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>4</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex pf-m-space-items-xs">
                                  <div class="pf-v5-l-flex__item">
                                    <i class="fas fa-times-circle" aria-hidden="true"></i>
                                  </div>
                                  <div class="pf-v5-l-flex__item">
                                    <span>1</span>
                                  </div>
                                </div>
                                <div class="pf-v5-l-flex__item">Updated 2 days ago</div>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v5-c-data-list__cell pf-m-align-right pf-m-no-fill">
                            <button class="pf-v5-c-button pf-m-secondary" type="button">Action</button>
                            <button class="pf-v5-c-button pf-m-link" type="button">Link</button>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
  
              <!-- Panel -->
              <div class="pf-v5-c-drawer__panel">
                <!-- Panel header -->
                <div class="pf-v5-c-drawer__body">
                  <div class="pf-v5-l-flex pf-m-column">
                    <div class="pf-v5-l-flex__item">
                      <div class="pf-v5-c-drawer__head">
                        <div class="pf-v5-c-drawer__actions">
                          <div class="pf-v5-c-drawer__close">
                            <button class="pf-v5-c-button pf-m-plain" type="button" aria-label="Close drawer panel">
                              <i class="fas fa-times" aria-hidden="true"></i>
                            </button>
                          </div>
                        </div>
                        <h2 class="pf-v5-c-title pf-m-lg" id="primary-detail-expanded-example-drawer-drawer-label">Node 2
                        </h2>
                      </div>
                    </div>
                    <div class="pf-v5-l-flex__item">
                      <a href="#">siemur/test-space</a>
                    </div>
                  </div>
                </div>
  
                <!-- Tabs -->
                <div class="pf-v5-c-drawer__body pf-m-no-padding">
                  <div class="pf-v5-c-tabs pf-m-box pf-m-fill" role="region"
                    id="primary-detail-expanded-example-drawer-tabs">
                    <button class="pf-v5-c-tabs__scroll-button" type="button" aria-label="Scroll left">
                      <i class="fas fa-angle-left" aria-hidden="true"></i>
                    </button>
                    <ul class="pf-v5-c-tabs__list" role="tablist">
                      <li class="pf-v5-c-tabs__item pf-m-current" role="presentation">
                        <button type="button" class="pf-v5-c-tabs__link" role="tab"
                          aria-controls="primary-detail-expanded-example-drawer-tabs-tab1-panel"
                          id="primary-detail-expanded-example-drawer-tabs-tab1-link">
                          <span class="pf-v5-c-tabs__item-text">Overview</span>
                        </button>
                      </li>
                      <li class="pf-v5-c-tabs__item" role="presentation">
                        <button type="button" class="pf-v5-c-tabs__link" role="tab"
                          aria-controls="primary-detail-expanded-example-drawer-tabs-tab2-panel"
                          id="primary-detail-expanded-example-drawer-tabs-tab2-link">
                          <span class="pf-v5-c-tabs__item-text">Activity</span>
                        </button>
                      </li>
                    </ul>
                    <button class="pf-v5-c-tabs__scroll-button" type="button" aria-label="Scroll right">
                      <i class="fas fa-angle-right" aria-hidden="true"></i>
                    </button>
                  </div>
                </div>
  
                <!-- Tab content -->
                <div class="pf-v5-c-drawer__body">
                  <section class="pf-v5-c-tab-content" id="primary-detail-expanded-example-drawer-tabs-tab1-panel"
                    aria-labelledby="primary-detail-expanded-example-drawer-tabs-tab1-link" role="tabpanel" tabindex="0">
                    <div class="pf-v5-c-tab-content__body">
                      <div class="pf-v5-l-flex pf-m-column pf-m-space-items-lg">
                        <div class="pf-v5-l-flex__item">
                          <p>The content of the drawer really is up to you. It could have form
                            fields,
                            definition lists, text lists, labels, charts, progress bars, etc.
                            Spacing recommendation is 24px margins. You can put tabs in here,
                            and
                            can also make the drawer scrollable.</p>
                        </div>
                        <div class="pf-v5-l-flex__item">
                          <div class="pf-v5-c-progress pf-m-sm"
                            id="primary-detail-expanded-example-drawer-progress-example1">
                            <div class="pf-v5-c-progress__description"
                              id="primary-detail-expanded-example-drawer-progress-example1-description">
                              Capacity</div>
                            <div class="pf-v5-c-progress__status" aria-hidden="true">
                              <span class="pf-v5-c-progress__measure">33%</span>
                            </div>
                            <div class="pf-v5-c-progress__bar" role="progressbar" aria-valuemin="0" aria-valuemax="100"
                              aria-valuenow="33"
                              aria-labelledby="primary-detail-expanded-example-drawer-progress-example1-description"
                              aria-label="Progress 1">
                              <div class="pf-v5-c-progress__indicator" style="width:33%;">
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="pf-v5-l-flex__item">
                          <div class="pf-v5-c-progress pf-m-sm"
                            id="primary-detail-expanded-example-drawer-progress-example2">
                            <div class="pf-v5-c-progress__description"
                              id="primary-detail-expanded-example-drawer-progress-example2-description">
                              Modules</div>
                            <div class="pf-v5-c-progress__status" aria-hidden="true">
                              <span class="pf-v5-c-progress__measure">66%</span>
                            </div>
                            <div class="pf-v5-c-progress__bar" role="progressbar" aria-valuemin="0" aria-valuemax="100"
                              aria-valuenow="66"
                              aria-labelledby="primary-detail-expanded-example-drawer-progress-example2-description"
                              aria-label="Progress 2">
                              <div class="pf-v5-c-progress__indicator" style="width:66%;">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </section>
                  <section class="pf-v5-c-tab-content" id="primary-detail-expanded-example-drawer-tabs-tab2-panel"
                    aria-labelledby="primary-detail-expanded-example-drawer-tabs-tab2-link" role="tabpanel" tabindex="0"
                    hidden>
                    <div class="pf-v5-c-tab-content__body">Panel 2</div>
                  </section>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  </body>
</body>
