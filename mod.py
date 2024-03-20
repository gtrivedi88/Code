:_mod-docs-content-type: PROCEDURE

[id="customizing-sample-pipelines_{context}"]
= Customizing sample pipeline templates

Learn about pipeline customization to cutsomize pipelines and associated tasks based on you organizations needs.


So you can customize the pipelines.
We provide two repos.

1. repo for sample pipelines https://github.com/pipelines

2. repo for sample template https://github.com/templates

We suggest you fork and clone these repositories for further customization.


.Prerequisites

* You have already forked and cloned the pipeline repository locally.
* You have already forked and cloned the templates repository locally.

.Procedure

Changes to make in your template:

. Open your templates repository that you cloned locally and expand the skeleton directory. There you see the three subdirectories `backstage`, `gitops-template`, and `source-repo`.

. Expand `gitops-template` > `.tekton`, and then select `gitops-on-pull-request.yaml`.

. Update the `pac` URL with the location of your forked pipeline repository url.

+
.The `pac` URLS
image::pac_url[]

. Expand `source-repo` > `.tekton`, and then update:

.. The `pac` URLs in the `docker-pull-request.yaml` file with the location of your forked pipeline repository url.
+
.The `docker-pull-request.yaml` URLS
image::docker_pull_request.png[]

.. The `pac` URLs in the `docker-push.yaml` file the location of your forked pipeline repository url.
+
.The `docker-push.yaml` URLS
image::docker_push.png[]

. Commit and push the updates


Changes that you make in your pipelines repository

. Organization have different workflow and requirements. Based on your workflow and requirements you can update the pipeline repository to:

* Add or update existing tasks. Expand `pac` > `tasks` directory.

* Behaviour of pull and push requests. Expand `pac` > `docker-build-rhtap` directory.

* Behavvior of the GitOps repository. Expand `pac` > `gitops-repo`.

* Behaviour of the source repo. Expand `pac` > `source-repo`.

. 
.Verification

* Consider creating an application to explore the impact of your template and pipeline customization.

[role="_additional-resources"]
.Additional resources

* To customize templates, see xref:customizing-sample-software-templates_{context}[Customizing sample software templates]

