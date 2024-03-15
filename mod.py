:_newdoc-version: 2.16.0
:_template-generated: 2024-03-12
:_mod-docs-content-type: PROCEDURE

[id="deploy-application-and-view-security-insights_{context}"]
= Deploy application and view security insights

Organizations typically follow a structured process for deploying applications, moving from development through pre-production to production. This process is often automated and regulated by defined rules and triggers.

This guide illustrates deploying applications using ArgoCD in OpenShift GitOps, facilitating continuous deployment across all stages. Deployment initiation requires updates to the GitOps repository.

[NOTE]
====
This deployment approach is an example; organizations may adopt any method that suits their workflow.
====

[Discrete]
== Promoting a build to a pre-production or production environment

Promoting a build to the pre-production or production environment involves updating the GitOps repository through `push` or `pull` requests in your repository, which in turn triggers a Tekton pipeline.

. Open the repository that you cloned when initiating a build pipeline.

+
[NOTE]
====
Ensure that the local clone is up-to-date
====

. Trigger the promotion pipeline through a `push` or `pull` request, with pull requests being the preferred method.

.. If your application is on development environment, run the following command to promote it to staging environment. The promotion pipeline interprets the messages in these commands to execute the corresponding promotion.

+
[options="nowrap"]
----
git commit --allow-empty -m "/promote dev"
----

.. If your application is on stanging environment, run the following command to move it to production environment. The promotion pipeline interprets the messages in these commands to execute the corresponding promotion.

+
[options="nowrap"]
----
git commit --allow-empty -m "/promote stage"
----

. Execute `git push`.

.Verification

. Navigate to the *CD* tab and review the ArgoCD history.

.  Various columns display the latest updates, showing the application's (for example, `appname-prod`) current status , deployment details, author, commit message (for example, Promote stage to prod), and the container image promoted to production.

. You can also, navigate to the *Topology* tab to view your application in various namespaces.

= View security insights

The promotion pipeline run offers a visual representation of all the tasks in a pipeline. A *green* status indicates successful completion, streamlining your workflow without extensive oversight.

The initial build pipeline tasks comprise:

* *`clone-repository`*: Clones the specified repository into the workspace, readying it for action with the git-clone Task.

* *`verify-enterprise-contract`*: enhances security by validating container images ensuring they originates from a corporate standard or approved build system. This task leverages the Enterprise Contract (EC) policies, a command-line interface that works along side Sigstore’s cosign, to assess the integrity of image signatures and attestations.

* *`handle-promotion-action`*: it extracts the container images based on your commit message, for example from development environment or standing environment, and then again based on your commit message, pushes these images to the appropriate environments, for example from development environment or standing environment



== Enterprise contract task

The Enterprise Contract is a set of tools for maintaining software supply chain security, and for the definition and enforcement of policies related to how container images are built and tested.

The Enterprise Contract’s purpose is to ensure container images produced by AppStudio meet certain clearly defined requirements before they are considered releasable. Should a container image not meet the requirements the Enterprise Contract will produce a list of the reasons why so they can be addressed as required to produce a releasable build.

The Konflux build process uses Tekton Chains to produce a signed in-toto attestation of the build pipeline. Enterprise Contract then uses that signed attestation to cryptographically verify that the build was not tampered with, and to check the build against a set of policies. The policies attest that the build process followed a prescribed set of best practices, plus organization specific policies as required.

For more information on Enterprise Contract, refer <Doc on which Jocelyn is working>.
