:_mod-docs-content-type: PROCEDURE

[id="update-application-and-view-security-insights_{context}"]
= Update application and view security insights

[role="_abstract"]
After successfully building your component with {ProductShortName}, the next step is to update your application and delve into the security insights.

== Initiating code updates

With {ProductShortName}, this process is straightforward. 

. Select *Catalog* and then select an appropriate component for which you want to view security insights.

. On the *Overview* tab, select *View Source*. This system displays the GitLab or GitHub UI for your repository.
On the overview tab you can also click "View Tech Docs" to view the documentation. If you remember, we mentioned the phrase "docs as code" earlier in the session, that is handled as markdown files within the codebase. You might be wondering from where the techdocs are coming from. Well when you clicked View source to view the repository, you would see a docs folder inside the repo, this is doc-as-code. You can update the content there and the changes will reflected in the Tech Docs after when the pipeline run is successfully completed.

== Making changes to your code

With access to your repository, you're ready to engage in the familiar process of working with a git repository. Here's how to proceed:

* *Clone* your repository to your local machine or development environment.
* *Modify* the application code as needed to introduce new features, fix bugs, or improve performance. For example, you may want to update tech docs or index.html 
* *Push* the changes back to the repository to update your application.

After pushing the updates, on RHDH, you might want select Image Registry tab to view to know how everything provisioned, in the case of this template, it uses ArgoCD for Namespace, application and even pipeline provisioning leveraging GitOps and a gi repo as the source of truth.

These steps are foundational to applying updates and leveraging the security features of {ProductShortName}. After making the necessary changes and addressing security insights, commit your changes with a meaningful message and push them to the repository. This update triggers the RHTAP pipeline, allowing you to witness the application's path to production and the activation of security measures.

=== Exploring different ways to update code

{ProductShortName} accommodates various development workflows, allowing you to make code changes and trigger security-focused pipelines through:

* The *GitLab or GitHubUI*, for direct modifications within the web interface.
* *Dev Spaces*, offering an integrated development environment within OpenShift.
* A *local IDE* on your laptop, for a traditional code development experience.

=== Exploring Dev Spaces - An Integrated Development Experience

Dev Spaces provides a Kubernetes-native workspace and IDE capability, streamlining the development process with zero configuration effort from the developers' end. To access Dev Spaces:

. Select *Catalog* and then select an appropriate component.
. On the *Overview* tab, select *OpenShift Dev Spaces (VS Code)*. This approach simplifies code updates and enhances the overall development experience.

=== Dependency analytics
With the Dependency Analytics plugin, available for both VS Code and JetBrains IntelliJ, developers gain early warnings about potential security vulnerabilities directly in the IDE. This feature is crucial for preemptively addressing security concerns before they impact your application.

I was hired to be an enterprise Java developer and I know the Quarkus framework, the super fast, super lightweight, optimized for cloud native microservices runtime. So let’s look at that Java code and make a change.

Note: If you have the Dependency Analytics plug-in installed then you can attempt the next section.

As an application developer, my favorite keys on the keyboard are Cntrl-C and Cntrl-V (or Command-C and Command-V for Mac-users). The magic of copy & paste is how I function as a developer. When I have a question, I go ask Google, perhaps these days it might be ChatGPT, but I ask the internet and the internet responds. In many cases, I am sent to StackOverflow and I find great things to copy & paste. For instance, what if I wanted a nice Model-View-Controller framework or perhaps a logging framework, they are easily found via Google, StackOverflow and a quick visit to Maven Central.

Maven Central

Open the pom.xml and add in the following dependencies

        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.14.1</version>
        </dependency>

        <dependency>
            <groupId>org.apache.struts</groupId>
            <artifactId>struts2-core</artifactId>
            <version>2.5.2</version>
        </dependency>

The Log4J vulunerability is particularly interesting. You might even remember where you were in December of 2021 when the Log4shell news broke. I have talked to a number of big companies that had folks running around with their hair on fire - "where is log4j?". The vulnerable code had been in the codbase for 8 years. It is a very widely deployed Java library as a very popular logging framework. Apparently someone thought it would be clever to add a JNDI feature eons ago. Well an Alibaba engineer that discovered that this code could be exploited for remote execution in Nov of 2021. They properly alerted the Apache Foundation and a patch was crafted. The problem with a zero day vulnerability is that you have zero days to react. The moment the patch is revealed means evil doers also become aware of the exploit - it becomes a race to see who can patch versus who will be exploited.

You should see some small red squiggles

code change code 13
This is the Dependency Analytics IDE plug-in providing an early warning signal. Remember we said that at Red Hat we aim to help you better secure your software supply chain across your SDLC, from code, to build, through deployment and into the runtime environment. In this case, the IDE plug-in is helping the developer to head off a problem BEFORE it enters your enterprise supply chain. Red Hat will be doing more in this area to provide recommendations in the future. As you can see we are partnered with

code change code 14
You can manually open the report tab by clicking on the "Found N vulnerabilities" at the bottom of VS Code.

== View security insights
