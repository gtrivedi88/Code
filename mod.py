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
a|Set this to your on-prem GitHub host. Default is `github.com`.

|export GITLAB__DEFAULT__HOST
a|Set this to your on-prem GitLab host. Default is `gitlab.com`.

|export QUAY__DEFAULT__HOST
a|The default Quay URL correspond to your specific on-prem environment. The default quay host is `quay.io`.

|export DEFAULT__DEPLOYMENT__NAMESPACE__PREFIX
a|The namespace prefix for deployments within {ProductShortName}. Default is `rhtap-app`.

NOTE: Update this if you have modified the default `trusted-application-pipeline: namespace` during the {ProductShortName} installation process. If you want to change the deployment namespace post-installation, follow Step 5.

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

. Commit your changes and push them to your repository. This update automatically refreshes the default templates in {RHDHShortName} with your custom values. Alternatively, on the {RHDHShortName} platform you can import and refresh a single or all customized templates. To import and refresh a single or all customized templates:

.. Navigate to *Create* > *Register Existing Component*.

.. If you are importing a single customized template, on your forked template repository, navigate to `templates` directory, select `template.yaml` and from the broweser address bar copy the we address. For example, https://github.com/<username>/tssc-sample-templates/blob/main/templates/devfile-sample-code-with-quarkus-dance/template.yaml. If you are importing all the customized teamplates, select `all.yaml` and broweser address bar copy the we address. For example, https://github.com/<username>/tssc-sample-templates/blob/main/all.yaml

.. On the {RHDHShortName} platform, in the Select URL field, enter either the URL for a single template or for all tyhe templates.

.. Select Analyze and select Import. The system import and refresh a single or all customized templates in the {RHDHShortName}

. (Optional) For changes made to the deployment namespace post-installation:

.. Log in to the OpenShift web console, in the Administrator perspective, create a new namespace.

.. Run the `PipelineRun` within this new namespace.

.Verification

* Test the effectiveness of your customizations by initiating a new application project. This ensures your adjustments are correctly applied and operational within the on-prem environment.

[role="_additional-resources"]
.Next steps

* Create an application.
