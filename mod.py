:_mod-docs-content-type: PROCEDURE

[id="customizing-sample-pipelines_{context}"]
= Customizing sample pipelines

Customizing sample pipelines and workflows enables organizations to align development practices with specific requirements. This section outlines the steps to personalize pipeline template and adapt pipeline configurations to your organizational needs.

.Prerequisites

* You have already forked and cloned both the link:https://github.com/redhat-appstudio/tssc-sample-pipelines[sample pipelines] and link:https://github.com/redhat-appstudio/tssc-sample-templates[sample software templates] repositories locally.

[discrete]
== Customizing the sample software template repository to update Pipeline as code (`pac`) URLs*

.Procedure

. Access your forked sample pipelines repository and copy the URL from the web address bar. For example, https://github.com/<username>/tssc-sample-pipelines.

. Access the cloned sample templates repository and in terminal run the following command:

+
[source,bash]
----
.scripts/update-tekton-definition <your-sample-pipeline-fork-url> <your-sample-pipeline-branch>

# For example, .scripts/update-tekton-definition https://github.com/<username>/tssc-sample-pipelines main
----

. Review and commit the changes and push them to your repository, effectively updating the templates.
