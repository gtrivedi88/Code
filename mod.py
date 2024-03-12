Code Change & Pipeline
As a developer, I want to get into the code so I will click Source Code Repository

code change 1
This opens the GitLab UI for the newly generated repository.

code change 2
I know what to do with a git repo, I clone it, I change it!

Narrator: There are at least 3 different ways to make a change to this source and and see the SSCS-focused pipeline triggered.

The developer could use the GitLab UI.

The developer could use Dev Spaces

The developer could use a local IDE on their laptop.

For the purposes of this demonstration, let’s try Dev Spaces.

Note: The Dependency Analytics plug-in for VS Code is available

VS Code

Jetbrains IntelliJ

Dev Spaces
Going back to Developer Hub tab, click Open Component in catalog

code change 3
Developer: I saw all the logging fly by and now I am interested in exploring this new software component.

After I open the Component I can click OpenShift Dev Spaces (VS Code)

Narrator: Dev Spaces is a Kubernetes native workspace and IDE capability that is part of the OpenShift platform. This tool allows your platform team to offer dynamic in-cluster IDE that requires zero configuration and effort by your app developers.

code change dev spaces 1
code change dev spaces 2
code change dev spaces 3
code change dev spaces 4
code change dev spaces 5
code change dev spaces 6
code change dev spaces 7
code change dev spaces 8
Code Exploration
Narrator: Early when we were exploring the Catalog, you might have been wondering what the magic was, how did the git repo become part of the Catalog? A key file is called catalog-info.yaml

code change code 1
A deeper dive session will be needed to drill-down into this yaml file along with more information on how Backstage Templates execute.

If you remember, we mentioned the phrase "docs as code" earlier in the session, that is handled as markdown files within the codebase.

code change code 2
Developer: As part of the interview process, I remember that this team described how they like to handle docs. They leverage the creation of markdown files inside of a docs folder within the code repository and the template pre-populated the repository for me. For now, I am just going to add a wee bit of markdown to see how this shows up later inside the portal. Of course I will come back and create ample documentation because it is just another file inside of my IDE and inside of my repository.

code change code 3
For now, I want to dive into the code src/main/resources/META-INF/index.html Let me just make a change where it says "Congratulations". I will hit Cntrl-F and type "congrat"

code change code 4
I will make this say "Aloha Andrew"

code change code 5
I was hired to be an enterprise Java developer and I know the Quarkus framework, the super fast, super lightweight, optimized for cloud native microservices runtime. So let’s look at that Java code and make a change.

code change code 6
Dependency Analytics
Note: If you have the Dependency Analytics plug-in installed then you can attempt the next section.

As an application developer, my favorite keys on the keyboard are Cntrl-C and Cntrl-V (or Command-C and Command-V for Mac-users). The magic of copy & paste is how I function as a developer. When I have a question, I go ask Google, perhaps these days it might be ChatGPT, but I ask the internet and the internet responds. In many cases, I am sent to StackOverflow and I find great things to copy & paste. For instance, what if I wanted a nice Model-View-Controller framework or perhaps a logging framework, they are easily found via Google, StackOverflow and a quick visit to Maven Central.

Maven Central

code change code 12
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

code change code 15
Use Cntrl-Z/Command-Z to undo those changes. That is the other magical key combination.

Back to your regularly scheduled programming
Developer: OK, I have made some changes, I really should spend some time properly testing my code but what I really want to understand is the path-to-production and see the pipeline in action.

So let me check-in my code. Give it a commit message.

code change code 7
code change code 8
code change code 9
code change code 10
Now I want to jump back to the portal and let’s see what is happening.

code change code 11
The pipeline is running. As a developer, I onboarded to the corporate standard pipeline with no effort. I have only been working at this new company for a few hours having just received my new laptop and VPN access. And I am already seeing things run end-to-end.

Narrator: While that pipeline is running, let’s look behind the scenes to get a feel for how all this magic is happening. The Platform Engineer needs to better understand the magic.

If we go look at the git repository that the template generated and click on Settings then Webhooks we can see the pipeline is triggered by push, tag and release events.

explain pipeline magic 1
explain pipeline magic 2
Also, as a developer, I am curious to know how everything provisioned, in the case of this template, it uses ArgoCD for Namespace, application and even pipeline provisioning leveraging GitOps and a gi repo as the source of truth.

explain pipeline magic 3
Now, let’s go explore the pipeline
