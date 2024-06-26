{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to the Official Product List Manager!</h1>
{% endblock %}

{% block content %}
<!-- Row 1: Introductory Text and Rectangle -->
<div class="pf-v5-c-page__main-section">
    <div class="pf-v5-l-grid pf-m-gutter">
        <div class="pf-v5-l-grid__item pf-m-9-col">
            <h2 class="pf-v5-c-title pf-m-xl">Red Hat official product list</h2>
            <p>The official Red Hat product names list (OPL) documents Brand- and Legal-approved names for Red Hat
                products, services, operators, components, features, portals, tools, and programs, determined in
                coordination with product teams and business units.</p>
        </div>
        <div class="pf-v5-l-grid__item pf-m-3-col" style="display: flex; justify-content: center; align-items: center;">
            <div style="width: 679.248px; height: 201px; flex-shrink: 0; background-color: #D9D9D9;"></div>
        </div>
    </div>
</div>

<!-- Row 2: Search by Portfolio and Core Platforms -->
<div class="pf-v5-c-page__main-section">
    <div class="pf-v5-l-grid pf-m-gutter">
        <div class="pf-v5-l-grid__item pf-m-6-col">
            <div class="pf-v5-c-card" style="height: 100%;">
                <div class="pf-v5-c-title pf-v5-u-m-md">Search by portfolio</div>
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
            <div class="pf-v5-c-card" style="height: 100%;">
                <div class="pf-v5-c-title pf-v5-u-m-md">Core platforms</div>
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
                <div class="pf-v5-c-title pf-v5-u-m-md">Learn more about Red Hat's naming approach</div>
                <div class="pf-v5-c-card__body">
                    <p>Each entry provides the full official name, as well as a brief description, guidance on approved
                        and unapproved short names and acronyms, availability, links to additional resources, and
                        metadata (such as parent product and portfolio).</p>
                    <button class="pf-v5-c-button pf-m-secondary" type="button">Naming foundations</button>
                    <button class="pf-v5-c-button pf-m-secondary" type="button">Glossary</button>
                </div>
            </div>
        </div>
        <div class="pf-v5-l-grid__item pf-m-4-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-title pf-v5-u-m-md">Keep up with product changes</div>
                <div class="pf-v5-c-card__body">
                    <p>Every entry of the OPL includes a changelog for edits, corrections, and status updates. We’ve
                        also collected them into a feed for quick reference.</p>
                    <button class="pf-v5-c-button pf-m-secondary" type="button">View changelog</button>
                </div>
            </div>
        </div>
        <div class="pf-v5-l-grid__item pf-m-4-col">
            <div class="pf-v5-c-card">
                <div class="pf-v5-c-title pf-v5-u-m-md">Contact the Brand Design and Naming team</div>
                <div class="pf-v5-c-card__body">
                    <p>Submit edits and corrections, request a new product name, get help with product names.</p>
                    <button class="pf-v5-c-button pf-m-secondary" type="button">Find out how</button>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Footer Text -->
<footer class="pf-v5-c-page__main-section">
    <p>n</p>
</footer>
{% endblock %}
