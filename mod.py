name: GitHub Pages

on:
  push:
    branches: 
    - main
    - rhdh-1.**
    - 1.**.x

jobs:
  adoc_build:
    name: Asciidoctor Build For GH Pages
    runs-on: ubuntu-latest
    permissions:
      contents: write
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Setup environment
      run: |
        # update
        sudo apt-get update -y || true
        # install 
        sudo apt-get -y -q install asciidoctor && asciidoctor --version
        echo "GIT_BRANCH=${GITHUB_HEAD_REF:-${GITHUB_REF#refs/heads/}}" >> $GITHUB_ENV

    - name: Build guides and indexes
      run: |
        echo "Building branch ${{ env.GIT_BRANCH }}"
        build/scripts/build.sh -b ${{ env.GIT_BRANCH }}

    # repo must be public for this to work
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      # if: github.ref == 'refs/heads/main'
      with:
        github_token: ${{ secrets.RHDH_BOT_TOKEN }}
        publish_branch: gh-pages
        keep_files: true
        publish_dir: ./titles-generated

    - name: Cleanup merged PR branches 
      run: |
        PULL_URL="https://api.github.com/repos/redhat-developer/red-hat-developers-documentation-rhdh/pulls"
        GITHUB_TOKEN="${{ secrets.RHDH_BOT_TOKEN }}"
        git config user.name "rhdh-bot service account"
        git config user.email "rhdh-bot@redhat.com"

        git checkout gh-pages; git pull || true
        for d in $(find . -maxdepth 1 -name "pr-*" -type d); do 
          PR="${d#*pr-}"
          echo -n "Check merge status of PR $PR ... "
          if [[ $(curl -sSL -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" "$PULL_URL/$PR" | grep merged\") == *"merged\": true"* ]]; then
            echo "merged, can delete from pulls.html and remove folder $d"
            git rm -fr --quiet $d
            sed -r -e "/pr-$PR\/index.html>pr-$PR</d" -i pulls.html
          else
            echo "PR is unmerged (or could not read API)"
          fi
        done
        git commit -s -m "remove merged PR branches" .
        git push origin gh-pages
