= Update application and view security insights

[role="_abstract"]
After successfully building your component with {ProductShortName}, the next step is to update your application and delve into the security insights.

== Initiating code updates

With {ProductShortName}, this process is straightforward.

. Select *Catalog* and then select an appropriate component for which you want to view security insights.

. On the *Overview* tab, select *View Source* tab to see your project in GitLab or GitHub. Here, you can also select *View Tech Docs* to see your project's documentation. The source of the documentation is the `docs` directory in your repository. If you update these files and the pipeline runs successfully, your Tech Docs will update too.

If you are using a GitLab repository to make code updates, you need to manually step up the webhooks:

. Log in to the OpenShift web console.

. In the Administrator perspective, for `rhtap` project, expand Pipelines, and select `PipelineRuns`.

. Select `rhtap-pe-info-<>` pipeline run, and then select Logs.

+
[NOTE]
====
This step provides you the webhook URL and the . that you need to add in your GitLab repository.
====

. In an appropriate GitLab repository, go to Settings > Webhooks.

. In the URL field, enter the webhook URL that you got as part of Step 3.

. In the . Token field, enter the . that you got as part of Step 3.

. In the Trigger section, select Push events and Merge request events.

. On your terminal, run the following command:

+
[source,bash]
----
kubectl -n target-namespace create . generic gitlab-webhook-config --from-literal provider.token=<GITLAB_TOKEN> --from-literal webhook..=<WEBHOOK_.> # <1>
----
<1> The GITLAB_TOKEN is your personal GitLab account token. The WEBHOOK_. is the . that you got as part of Step 3.

. Add the following in your source repository CR yaml, under `.spec`

+
[source,yaml]
----
git_provider
    # URL: "https://gitlab.example.com" #Set this if you are using on-prem GitLab host.
on-prem GitLab host
    .:
        name: "gitlab-webhook-config"
        key: "provider.token"
    webhook-.:
        name: "gitlab-webhook-config"
        key: "webhook.."
----


== Making changes to your code

With access to your repository, you're ready to engage in the familiar process of working with a git repository. Here's how to proceed:

- **Clone** your repository to start working on it either locally or in your development environment.

- **Modify** your application, like updating technical docs or `index.html`, or by adding new features or bug fixes.

- *Commit* your changes.

- **Push** your changes to the repository.

After you update your component, the update automatically triggers the `on-push` pipeline. Depending on your workflow, this process might not only move your application closer to product but also engages the security measures, offering you a comprehensive view of the application's development journey.
