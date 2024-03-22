:_mod-docs-content-type: PROCEDURE

[id="build-an-application-with-sample-software-templates_{context}"]
= Build an application with sample software templates

{ProductShortName} introduces ready-to-use software templates in {RHDHShortName} to expedite your application's journey to production. These templates are meticulously designed for seamless integration with Red Hat's comprehensive suite of tools ({RHDHShortName}, {RHTASShortName}, {RHTPAShortName}) and technologies. This integration furnishes a solid framework for a secure, effective, and developer-oriented SDLC within an on-premises environment.

Beyond these foundational elements, {ProductShortName}’s software templates include default integrations with key technologies to further secure and optimize your development lifecycle:

* *ACS (Advanced Cluster Security):* Bolsters your deployments by identifying and mitigating vulnerabilities early in the development process, ensuring your applications are fortified from inception to deployment.

* *Quay:* Acts as a secure harbor for your container images, providing a reliable repository that continuously scans for vulnerabilities, keeping your containerized applications safe.

* *Tekton Pipelines:* Automates your build and deployment processes with precision, enabling a CI/CD framework that integrates seamlessly into your SDLC, thus accelerating your path to production.

* *GitOps:* Implements a GitOps strategy by maintaining your infrastructure and application configurations in Git repositories, ensuring consistent and automated deployment across all environments.

Additionally, {ProductShortName} supports the development and containerization of applications across a wide range of popular programming languages such as Java, Python, Node.js, and Go, expanding your application development capabilities.

Upon the installation of {ProductShortName}, cluster administrators have the capability to tailor the {RHDHLongName} portal with specific templates and enhancements. This customization process is crucial for enabling developers to focus primarily on coding by simplifying development workflows and mitigating concerns related to pipelines, vulnerabilities, and policies.

Before proceeding with customization, it's essential for cluster administrators to familiarize themselves with the available software and pipeline templates through this guide. Such exploration is key to grasping how {ProductShortName} supports a secure supply chain, laying the groundwork for any subsequent customization.

== Setting the stage

* Ensure you have successfully installed {ProductShortName}.
* Log into {RHDHLongName} using the link provided by {ProductShortName}. {RHDHShortName} operates as an inclusive developer platform, facilitating the creation of developer portals. It offers engineering teams a unified platform that enhances the development process, providing an assortment of tools and resources for crafting high-quality software efficiently.

== Build an application

Building an application or microservice for your developers in {RHDHShortName} using the templates offered by {ProductShortName} is essentially only a three step process:

* Provide application information

* Provide application repository information

* Provide deployment information

*To create an application or microservice*

* On the {RHDHShortName} portal, select *Create*, and then select an appropriate template. For example, Quarkus Java - Trusted Application Pipeline.

[discrete]
=== Provide application information

. In the *Name* field, enter a name consisting of a sequence of alphanumeric characters ([a-zA-Z0-9]), allowing for separators of dashes (-), underscores (_), or periods (.) between them. The name must contain at least 1 character and no more than 63 characters in total.

. From the *Owner* dropdown list, select an appropriate RHDH component owner for this application. The default value is `user:guest`, which appears if no specific owner is registered in the system. If you have not registered an owner, retain the default `user:guest` selection. If needed, you have the option to replace `guest` with your username, personalizing ownership of the application.

. Select *Next*. The system displays the Application Repository Information form.

[discrete]
=== Provide application repository information

. From the *Host Type* dropdown list, select an appropriate repository host type.

. In the *Repository Owner* field, enter name of the organization that owns the Git App you are using. This could be a personal user account, an organization, or a project within your organization.

. In the *Repository Name* field, enter an appropriate repository name using characters restricted to A-Z, a-z, 0-9, underscore (_), and dashes (-). The system uses this information to name the repository that it creates on the host repository server.

. In the *Repository Default Branch* field, enter the default branch for your repository. This field displays `main` by default you can choose to keep it the same.

. In the *Repository Server* field, enter your on-prem host URL without the `HTTP` protocol and without the `.git` extension. For example, gitlab-gitlab.apps.cluster-ljg9z.sandbox219.opentlc.com

.  Select *Next*. The system displays the Deployment Information form.

[discrete]
=== Provide deployment information

. In the *Image Registry* field, enter your on-prem image registry URL without the `HTTP` protocol. For example, quay-tv2pb.apps.cluster-tv2pb.sandbox1194.opentlc.com.

. In the *Image Organization* field, enter the image organization for the image registry you provided in the Step 1.

. In the *Image Name* field, enter an appropriate image name following these guidelines: use only lowercase letters, dights, and separators. Separators include a period (.), up to two underscores (_), or one or more hyphens (-). For example, `my-app_1.2`.

+
[NOTE]
====
You must ensure that the name does not start or end with a separator. 
====

. In the *Deployment Namespace* field, enter the prefix for the namespaces or cluster where your intend to deploy your application. The system creates the actual namespaces as `rhtap-app-development`, `rhtap-app-stage`, and `rhtap-app-prod`.

+
[NOTE]
====
`rhtap-app` is the default deployment namespace prefix. Cluster administrators have the option to customize this prefix. For instructions on how to customize the default deployment namespace prefix, refer <tbd>.
====


. Select *Review* to review all the information that you added.

. Select *Create*. The system displays a visual representation of the tasks it performs when creating your application. A "green" status for each task indicates a successful pass through all checks, simplifying your development workflow by minimizing the need for detailed oversight.


== Review your application

After creating your application, you can easily review its components, source code, and associated documentation directly within the system. Follow these steps for a comprehensive overview:

* *Access Your Application*: To find your application, select *Open Component in catalog*. You can also navigate to the *Catalog* where the system lists your newly created application.

* *Examine the Source Code*:
    - Navigate to the *Overview* tab.
    - Click *View Source* to review the application's source code. This allows you to see the underlying code and understand how your application is built.

* *Review the Documentation*:
    - While on the *Overview* tab, select *View Tech Docs*.
    - This action opens the technical documentation associated with your application, offering insights into its functionality, configuration, and usage.

These steps are designed to provide a thorough understanding of your application, from its codebase to its technical documentation, ensuring you have all the necessary information for further development or deployment.

[role="_additional-resources"]
.Next steps

* xref:update-application-and-view-security-insights_{context}[Update application and view security insights]
