---
name: ROOT
title: Konflux-CI
version: ~
nav:
- modules/ROOT/pages/discover/_nav.adoc
- modules/ROOT/pages/getting-started/_nav.adoc
- modules/ROOT/pages/how-tos/_nav.adoc
- modules/ROOT/pages/advanced-how-tos/_nav.adoc
- modules/ROOT/pages/glossary/_nav.adoc
- modules/ROOT/pages/contribute/_nav.adoc

# Copyright 2022 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

---
runtime:
  cache_dir: ./.cache/antora
  log:
    failure_level: warn
site:
  title: Konflux-CI Documentation
  url: https://konflux-ci.dev/docs/discover
  robots: allow
content:
  sources:
    - url: .
      start_path: docs
      branches: HEAD
ui:
  bundle:
    url: https://gitlab.com/antora/antora-ui-default/-/jobs/artifacts/HEAD/raw/build/ui-bundle.zip?job=bundle-stable
    snapshot: true
  supplemental_files: ./antora-lunr-ui
output:
  dir: ./public

antora:
  extensions:
  - '@antora/collector-extension'
  - '@antora/lunr-extension'

urls:
    html_extension_style: indexify # For consistency with pages indexed by search engines, see https://docs.antora.org/antora/latest/playbook/urls-html-extension-style/
    redirect_facility: static # The least convenient, but only available redirect on our hosting platform, see https://docs.antora.org/antora/latest/playbook/urls-redirect-facility/
    latest_prerelease_version_segment: next # Override the version in the navigation https://docs.antora.org/antora/latest/playbook/urls-redirect-facility/
    latest_version_segment_strategy: replace # Consequence of static redirect, see https://docs.antora.org/antora/latest/playbook/urls-redirect-facility/

