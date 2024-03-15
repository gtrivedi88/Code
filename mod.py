---
image: registry.access.redhat.com/ubi9/ubi

cache:
  - key: $CI_COMMIT_REF_SLUG
    paths:
      - node_modules/
      - /root/.cache/

variables:
  NODE_AUTH_TOKEN: $NODE_AUTH_TOKEN
  CACHE_FALLBACK_KEY: main

test:
  stage: test
  before_script:
    - dnf module enable -y nodejs:18
    - dnf install -y nodejs golang jq
  script:
    - npm ci
    - npm run build-production
  artifacts:
    paths:
      - public
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  tags: [docker]

pages:
  stage: deploy
  before_script:
    - dnf module enable -y nodejs:18
    - dnf install -y nodejs golang jq
  script:
    - npm ci
    - npm run build-production
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  tags: [docker]
