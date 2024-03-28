#!/bin/bash

BRANCH="${CI_COMMIT_REF_NAME:-main}"
OUTPUT_DIR="titles-generated"
INDEX_FILE="${OUTPUT_DIR}/index.html"

# Ensure the output directory exists
mkdir -p "${OUTPUT_DIR}/${BRANCH}"

cp -r images/ "${OUTPUT_DIR}/${BRANCH}"

# Start of the HTML structure with a top navbar and site title
cat <<EOF > "${INDEX_FILE}"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The RHTAP Documentation Site</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body { padding-top: 56px; }
        .navbar-brand img { height: 30px; }
        .main-content { padding: 20px; }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="#">
        <img src="./${BRANCH}/images/logo.jpeg" alt="Logo"> The RHTAP Documentation Site
    </a>
</nav>

<div class="container main-content">
    <div class="row">
        <div class="col-12">
            <h1>Welcome to The RHTAP Documentation Site</h1>
            <h4>Select a topic to get started:</h4>
            <br><br>
            <a href="./${BRANCH}/release_notes/index.html" class="btn btn-primary">Release Notes</a>
            <br><br>
            <a href="./${BRANCH}/install/index.html" class="btn btn-primary">Install RHTAP</a>
            <br><br>
            <a href="./${BRANCH}/getting_started/index.html" class="btn btn-primary">Getting Started Guide</a>
            <br><br>
            <a href="./${BRANCH}/managing_ec/index.html" class="btn btn-primary">Managing Enterprise Contract</a>
            <a href="./${BRANCH}/managing_sboms/index.html" class="btn btn-primary">Managing SBOMs</a>
            <a href="./${BRANCH}/customizing_rhtap/index.html" class="btn btn-primary">Customizing RHTAP</a>
            

        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
EOF

# Process AsciiDoc files to HTML, as previously described
for t in titles/*/*.adoc; do
    guide_name=$(basename "$(dirname "$t")")
    output_subdir="${OUTPUT_DIR}/${BRANCH}/${guide_name}"
    mkdir -p "${output_subdir}"
    asciidoctor -b html5 -o "${output_subdir}/index.html" "$t"
done
