:_mod-docs-content-type: PROCEDURE

[id="customizing-sample-software-templates_{context}"]
= Customizing sample software templates

Learn how to customize ready-to-use software templates for your on-prem environment. Cluster administrators have full control over this process, including modifying metadata and specifications.

.Prerequisites

* You have used the forked repository URL from link:https://github.com/redhat-appstudio/tssc-sample-templates[tssc-sample-templates] during the {ProductShortName} install process.

.Procedure

. Clone your forked repository, and then open it in your preferred text editor, such as Visual Studio Code.

. Locate the *properties* file within your project directory. This file stores the default values that can customize. Open it for editing and update the following key-value pairs according to your environment.

+
[cols="1,1"]
|===
|Key |Description

|export GITHUB__DEFAULT__HOST
|Set this to your on-prem GitHub host. Default is `github.com`.

|export GITLAB__DEFAULT__HOST
|Set this to your on-prem GitLab host. Default is `gitlab.com`.

|export QUAY__DEFAULT__HOST
|The default Quay URL correspond to your specific on-prem environment. The default quay host is `quay.io`.

|export DEFAULT__DEPLOYMENT__NAMESPACE__PREFIX
|The default prefix used for deployment namespaces with in {ProductShortName}. The default deployment namespace prefix is `rhtap-app`. If you updated the default prefix used for deployment namespaces during the {ProductShortName} install process. You need to update that same value here. If you did not update the deployment namespace prefix during the install process you can do it now.

|===

+
.The properties file
image::properties.png[]

. Run the *generate.sh* script in your terminal. This action adjusts the software templates, replacing default host values with your specified inputs.

+
[source,terminal]
----
./generate.sh
----

+
.The generate.sh script
image::generate.png[]

. Commit your changes and push them to your repository. This update automatically refreshes the default templates in {RHDHShortName} with your custom values.

. (Optional) If you changed the default deployment namespace prefix after the install process:

.. Log in to the OpenShift web console, in the Administrator perspective, create a new namespace.

.. Run the `PipelineRun` in that namespace.

.Verification

* Test the effectiveness of your customizations by initiating a new application project. This ensures your adjustments are correctly applied and operational within the on-prem environment.

[role="_additional-resources"]
.Next steps

* Create an application.
