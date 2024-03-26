:_mod-docs-content-type: PROCEDURE

[id="webhook-configurations-for-gitlab_{context}"]
= Webhook Configurations for GitLab

*For GitLab users:* To automatically trigger pipeline executions upon code pushes, set up webhooks and secrets by following these steps:

. Log in to the OpenShift web console with Administrator privileges.

. Navigate to the `rhtap` project, expand *Pipelines*, and then select `PipelineRuns`.

. Select `rhtap-pe-info-<>` pipeline run, and then select *Logs* tab.

+
[NOTE]
====
These logs provide the webhook URL and the secret token required for GitLab configuration.
====

. Within your GitLab repository, navigate to *Settings* > *Webhooks*.

. In the *URL* field, enter the webhook URL obtained in Step 3.

. In the *Secret Token* field, enter the secret obtained in Step 3.

. In the *Trigger* section, select *Push events* and *Merge request events*.

. Select *Add Webhooks*.

.verification

* Update your code and review the automatically triggered pipeline run in the CI tab in {RHDHShortName}.
