:_mod-docs-content-type: PROCEDURE

[id="deploy-application-and-view-security-insights_{context}"]
= Deploy application and view security insights

Organizations leverage a structured approach for application deployment, typically involving development, pre-production, and production stages. This process is often automated and governed by defined rules and triggers.

This guide outlines deploying applications through ArgoCD in OpenShift GitOps, enabling continuous deployment across all stages. ArgoCD facilitates a GitOps-based deployment strategy, treading your Git repository as a single source of truth for your infrastructure configurations. Updates to this repository trigger deployments across environments.

[NOTE]
====
This guide shows an example deployment approach; organizations may adopt any method that suits their workflow.
====

== Promoting a build to a pre-production or production environment

Promoting a build to the pre-production or production environment involves updating the GitOps repository through `push` or `pull` requests in your repository, which in turn triggers a Tekton pipeline.

. On {RHDHShortName} platform, select *Catalog*.

. From the *Kind* dropdown list, select *Resource*, and then select an appropriate GitOps repository.

. On the Overview tab, select *View Source*.

. (Optional) Alternatively, select *Catalog*, and then on the *Overview* tab, select *View TechDocs*

.. In the Home > Repository section, select the GitOps repository.

. Clone your GitOps repository, and go to `component/<app-name>`.

+
[NOTE]
====
Ensure that the local clone is up-to-date
====

. Expand Overlays. The system displays `development`, `stage`, `prod` directories.

. Manually move an application from development environment to the stage or production environment.

+
[cols="1,1"]
|===
|To move your application|Do this

|From development to stage environment
|1. Expand `development` directory and select `deployment-patch.yaml`. 2. Copy the containers image URL. For example, quay.io/<username>/<app-name>/imageurl. 3. Go to `stage` directory, and select `deployment-patch.yaml`. 4. Paste the containers image URL to replace the existing one.  5. Commit and push your updates.

|From stage to production environment
|1. Expand `stage` directory and select `deployment-patch.yaml`. 2. Copy the containers image URL. For example, quay.io/<username>/<app-name>/imageurl. 3. Go to `prod` directory, and select `deployment-patch.yaml`. 4. Paste the containers image URL to replace the existing one.  5. Commit and push your updates.

|===


. This manual update triggers a promotion pipeline, that you can review in the *CI* tab in {RHDHShortName}

. Alternatively, not the prefered method though as it can skips some checks, you can automatically trigger the promotion pipeline through a `push` request, with pull requests being the preferred method.

+
* If your application is on development environment, run the following command to promote it to staging environment. The promotion pipeline interprets the messages in these commands to execute the corresponding promotion.
+
[options="nowrap"]
----
git commit --allow-empty -m "/promote dev"
----

+
* If your application is on staging environment, run the following command to move it to production environment. The promotion pipeline interprets the messages in these commands to execute the corresponding promotion.
+
[options="nowrap"]
----
git commit --allow-empty -m "/promote stage"
----

. Execute `git push`.

.Verification

. Navigate to the *CD* tab and review the ArgoCD history.

. Various columns display the latest updates, showing the application's (for example, `appname-prod`) current status , deployment details, author, commit message (for example, Promote stage to prod), and the container image promoted to production.

. You can also navigate to the *Topology* tab to visualize your application across various namespaces.
