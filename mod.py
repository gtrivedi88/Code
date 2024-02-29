= Retriggering Build Pipelines

Sometimes your build pipeline may flake out and you need to retrigger it. You can accomplish this on a pull request by adding comments to the pull request. You can accomplish this for post-merge builds by clicking a button in the UI, or by adding an annotation to your Component resource via the API.

See also xref:how-to-guides/testing_applications/proc_retriggering_integration_tests.adoc[Retriggering integration tests].

== Retriggering a pre-merge build on a pull request

.**Prerequisite**

- You have a build pipelinerun on a pull request that has failed and you want to re-run the build without pushing a new commit.
.**Procedure**

. Add a comment to the pull request with the text `/retest` which will trigger a new build.

You should see the pipelinerun start executing in the UI and in the pull request.

NOTE: See the link:https://pipelinesascode.com/docs/guide/running/#gitops-command-on-pull-or-merge-request[pipelinesascode documentation] for more options.

== Retriggering a post-merge build from your main branch from the UI

.**Prerequisite**

- You have already merged a pull request, but the build failed and you want to retrigger it.
.**Procedure**

In the console, complete the following steps to retrigger the build pipeline:

. Navigate to the *Activity* > *Pipeline runs* tab.
. Identify the pipelinerun that you want to retrigger.
. Select the three dots on the right side of the table.
. Select the *Rerun* action.

You should see the pipelinerun start executing back in the *Activity* > *Pipeline runs* tab.

== Retriggering a post-merge build from your main branch from the API

.**Prerequisite**

- You have already merged a pull request, but the build failed and you want to retrigger it.
- You have CLI access to {ProductName}. For information on obtaining CLI access, refer to  xref:../../getting-started/getting_started_in_cli.adoc[Getting started in CLI]
.**Procedure**

. Identify the *Component* whose pipeline needs to be rerun.
. Annotate the *Component* with `build.appstudio.openshift.io/request: trigger-pac-build`.
+
[source]
----
$ kubectl annotate components/[component name] build.appstudio.openshift.io/request=trigger-pac-build
----

. The build is re-triggered automatically.

+
[source]
----
$ tkn pipelinerun list
[Example Output]
NAME                            STARTED         DURATION   STATUS
your-component-jfrdb            4 seconds ago   ---        Running
----
