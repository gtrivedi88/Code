= Customizing {ProductName}

{ProductShortName}'s ready-to-use software templates and build pipeline runs offer predefined pathways that incorporate security practices directly into the development workflow. These templates significantly reduce the cognitive load on developers, enabling them to concentrate more on innovation and less on security-related concerns. 

Having said that, cluster administrators have the capability to:

* Customize ready-to-use software templates for their on-prem environment

* Customize build pipeline runs

This customization process is crucial for enabling developers to focus primarily on coding by simplifying development workflows and mitigating concerns related to pipelines, vulnerabilities, and policies.

include::topics/proc_customizing-sample-software-templates.adoc[leveloffset=+1]


= Customizing sample software templates

[role="_abstract"]

Learn how to customize ready-to-use software templates for your on-prem environment. 

As a cluster administrator you can customize each and every aspect of the ready-to-use software templates (for example, its metadata and specifications). Additionally, you can customize ready-to-use software templates for for your on-prem environment.

.Prerequisites

* You have used the forked link:https://github.com/redhat-appstudio/tssc-sample-templates[ready-to-use software templates] repository URL during the {ProductShortName} install process.

.Procedure

. Clone the forked repository and open it in the text editor of your choice, for example Visual Studio code.

. Open the *properties* file and update default host values for your on-prem host environment.

+
.The properties file
image::properties.png[]

. Run the *generate.sh* script on your terminal. This script updates the software template for all the instances of default host values with the values you provided.

+
[source,terminal]
----
./generate.sh
----

+
.The generate.sh script
image::generate.png[]

. Add, commit, and push the changes to the repository. The system automatically updates the default templates with updated values in {RHDHShortName}.

.Verification

* You can create a new application to verify the updates.
