== Making changes to your code

With access to your repository, you're ready to engage in the familiar process of working with a git repository. Here's how to proceed:

- **Clone** your repository to start working on it either locally or in your development environment.

- **Modify** your application, like updating technical docs or `index.html`, or by adding new features or bug fixes.

- *Commit* your changes, and push them to the repository.
- **Push** your changes to apply them.

After you update your component, the update automatically triggers the `on-push` pipeline. Depending on your workflow, this process might not only move your application closer to product but also engages the security measures, offering you a comprehensive view of the application's development journey.

To view the pipeline run:

. Switch back to {RHDH} platform
. Navigate to the *Catalog* and select the relevant component you wish to review.
. Open the *CI* tab to access the Pipeline Run section.
. (Optional) Select the *Image Registry* tab to see details about how everything is set up using ArgoCD and GitOps for smooth provisioning.
. (Optional) Select the *Topology* tab to view your application deployed in the development namespace. 


[discrete]
=== Exploring different ways to update code

{ProductShortName} accommodates various development workflows, allowing you to make code changes and trigger security-focused pipelines through:

* The *GitLab or GitHubUI*, for direct modifications within the web interface.
* *Dev Spaces*, offering an integrated development environment within OpenShift.
* A *local IDE* on your laptop, for a traditional code development experience.

[discrete]
=== Exploring Dev Spaces - An Integrated Development Experience

Dev Spaces provides a Kubernetes-native workspace and IDE capability, streamlining the development process with zero configuration effort from the developers' end. To access Dev Spaces:

. Select *Catalog* and then select an appropriate component.
. On the *Overview* tab, select *OpenShift Dev Spaces (VS Code)*. This approach simplifies code updates and enhances the overall development experience.

[discrete]
=== Enhancing code security with Dependency Analytics

The Dependency Analytics plugin, seamlessly integrated with *VS Code* and JetBrains *IntelliJ*, serves as your first line of defense against security vulnerabilities directly within your Integrated Development Environment (IDE). This powerful tool is designed to identify and address security risks early in the development process, ensuring a more secure application.

For example, as an adept Java developer exploring the capabilities of the Quarkus framework, the Dependency Analytics plugin becomes an invaluable asset. It empowers you to refine your Java code with an added layer of security, providing peace of mind as you enhance your application.

*Early Warning Signals for Vulnerabilities*

The Dependency Analytics IDE plugin excels in delivering timely alerts about potential security issues. This preemptive notification system is part of Red Hat's broader initiative to fortify the software supply chain at every stage — from initial code development through to build, deployment, and operational runtime. By intercepting potential problems before they can infiltrate your enterprise's supply chain, the plugin plays a crucial role in maintaining the integrity of your development lifecycle.

.Accessing vulnerability warnings and report
image::dependency-analytics-warning.png[]


*Comprehensive Security Insights with Dependency Analytics*

The plugin not only alerts developers to potential vulnerabilities but also provides detailed reports that offer insights into the security landscape of your application. These reports are instrumental in understanding the specific nature of each vulnerability, allowing developers to make informed decisions about how to proceed with mitigation.

.The Dependency Analytics report
image::dependency-analytics.png[]

By integrating the Dependency Analytics plugin into your development workflow, you're not just coding; you're embedding security into the very fabric of your application. This approach underscores the importance of security in modern software development, providing a stronger, more resilient foundation for your projects.

== Review your application

After updating your application, switch back to {RHDHShortName} platform and select Catalog and open the component on which you made the code change:

* 

* 
