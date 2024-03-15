image: ubuntu:latest

stages:
  - build
  - deploy

variables:
  GIT_STRATEGY: fetch

before_script:
  # Update package lists and install dependencies
  - apt-get update -y || true
  # Install asciidoctor for AsciiDoc processing and rsync for file operations
  - apt-get install -y asciidoctor rsync

build:
  stage: build
  script:
    # Ensure the build script is executable
    - chmod +x build.sh
    # Execute the build script, specifying the current branch name
    - ./build.sh -b $CI_COMMIT_REF_NAME
  # Specify the directory where the build output is located as artifacts
  artifacts:
    paths:
      - titles-generated/
  # Define rules to only run this job for main branch and specific patterns
  only:
    - main
  tags: [docker]

pages:
  stage: deploy
  script:
    # Prepare the public directory for GitLab Pages
    - mkdir -p public
    # Move the build output to the public directory, ensuring it's ready for GitLab Pages
    - mv titles-generated/* public/
  # Define the public directory as artifacts for GitLab Pages
  artifacts:
    paths:
      - public
  # Ensure this job runs only for the default branch (typically main)
  only:
    - main
  tags: [docker]
