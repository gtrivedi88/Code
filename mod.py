{% extends 'base.html' %}

{% block heading %}
<!-- Row 1: Introductory Text and Rectangle -->
<div class="pf-v5-c-page__main-section" style="background-color: #FFFFFF; margin-left: -20px;margin-top: -20px;margin-right: -24px !important;">
    <div class="pf-v5-l-grid pf-m-gutter">
            <h2 class="pf-v5-c-title pf-m-xl">Red Hat official product list</h2>
            <p class="pf-v5-c-content">
                The official Red Hat product names list (OPL) documents Brand- and Legal-approved names<br>
                for Red Hat products, services, operators, components, features, portals, tools, and<br>
                programs, determined in coordination with product teams and business units.
            </p>
    </div>
</div>
{% endblock %}

{% block content %}
<!-- Row 2: Search by Portfolio and Core Platforms -->
<div class="pf-v5-c-page__main-section">
    <div class="pf-v5-l-grid pf-m-gutter">
        <div class="pf-v5-l-grid__item pf-m-6-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-card__header">
                    <h3 class="pf-v5-c-title pf-m-lg">Search by portfolio</h3>
                </div>
                <div class="pf-v5-c-card__body">
                    <div class="label-container">
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Cloud</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Linux platforms</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Management</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Application services</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Edge and AI</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Professional services</span>
                            </button>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        <div class="pf-v5-l-grid__item pf-m-6-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-card__header">
                    <h3 class="pf-v5-c-title pf-m-lg">Core platforms</h3>
                </div>
                <div class="pf-v5-c-card__body">
                    <div class="label-container">
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Red Hat Enterprise Linux</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Red Hat OpenShift</span>
                            </button>
                        </span>
                        <span class="pf-v5-c-label pf-m-blue">
                            <button class="pf-v5-c-label__content" type="button">
                                <span class="pf-v5-c-label__text">Red Hat Ansible Automation Platform</span>
                            </button>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Row 3: Additional Cards -->
<div class="pf-v5-c-page__main-section">
    <div class="pf-v5-l-grid pf-m-gutter">
        <div class="pf-v5-l-grid__item pf-m-4-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-card__header">
                    <h3 class="pf-v5-c-title pf-m-lg">Learn more about Red Hat's naming approach</h3>
                </div>
                <div class="pf-v5-c-card__body">
                    <p>Each entry provides the full official name, as well as a brief description, guidance on approved
                        and unapproved short names and acronyms, availability, links to additional resources, and
                        metadata (such as parent product and portfolio).</p>
                    <div class="button-container">
                        <button class="pf-v5-c-button pf-m-secondary" type="button">Naming foundations</button>
                        <button class="pf-v5-c-button pf-m-secondary" type="button">Glossary</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="pf-v5-l-grid__item pf-m-4-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-card__header">
                    <h3 class="pf-v5-c-title pf-m-lg">Keep up with product changes</h3>
                </div>
                <div class="pf-v5-c-card__body">
                    <p>Every entry of the OPL includes a changelog for edits, corrections, and status updates. We’ve
                        also collected them into a feed for quick reference.</p>
                    <div class="button-container">
                        <button class="pf-v5-c-button pf-m-secondary" type="button">View changelog</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="pf-v5-l-grid__item pf-m-4-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-card__header">
                    <h3 class="pf-v5-c-title pf-m-lg">Contact the Brand Design and Naming team</h3>
                </div>
                <div class="pf-v5-c-card__body">
                    <p>Submit edits and corrections, request a new product name, get help with product names.</p>
                    <ul class="pf-v5-c-list">
                        <li>Submit edits and corrections</li>
                        <li>Request a new product name</li>
                        <li>Get help with product names</li>
                    </ul>
                    <div class="button-container">
                        <button class="pf-v5-c-button pf-m-secondary" type="button">Find out how</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}



<!doctype html>
{% include 'head.html' %}
<body>
  <div class="pf-v5-c-page">
    {% include 'masthead.html' %}
    {% include 'menu.html' %}
    <main tabindex="-1">
      <section class="pf-v5-c-page__main-section">
        {% block heading %}{% endblock %}
        {% block content %}{% endblock %}
      </section>
          {% block footer %}
          <footer class="pf-v5-c-page__main-section">
            <p class="pf-v5-c-about-modal-box__strapline">Red Hat confidential—Red Hat associates and approved NDA marketing
              agencies only—No further distribution</p>
          </footer>
          {% endblock %}
          </div>
    </main>
  </div>
</body>
