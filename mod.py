Assess your security posture 

bookmark_border
Security posture is an organization's ability to detect, respond to, and remediate threats. It includes the readiness of an organization's people, hardware, software, policies and processes across the entire software lifecycle.

There are a number of frameworks and tools that you can use to assess your security posture and identify ways to mitigate threats.

Software delivery practices
A strong security posture requires a strong foundation in software delivery best practices, and these practices go beyond implementing tools and technical controls. For example, if change approval process is unclear, then it is easier for unwanted changes to enter your software supply chain. If teams are discouraged from raising issues, they might hesitate to report security concerns.

DevOps Research and Assessment (DORA) performs independent research into practices and capabilities of high performance technology teams. To assess your team's performance and learn about ways to improve, use the following DORA resources:

Take the DORA DevOps Quick Check to get some quick feedback on how your organization compares with others.
Read about the technical, process, measurement, and cultural DevOps capabilities identified by DORA.
Frameworks for security posture
The NIST Secure Software Development Framework (SSDF) and Cybersecurity Assessment Framework (CAF) are frameworks developed by governments to help organizations assess their security posture and mitigate supply chain threats. These frameworks take into consideration the software development lifecycle as well as other aspects related to software security such as incident response plans. The complexity and scope of these frameworks can require a substantial investment in time and resources.

Supply chain Levels for Software Artifacts (SLSA) is a framework that aims to make assessment and mitigation implementation more approachable and incremental. It explains supply chain threats and associated mitigations and provides examples of tools to implement mitigations. It also groups requirements for strengthening your security posture in levels, so that you can prioritize and incrementally implement changes. SLSA is primarily focused on the software delivery pipeline, so you should use it together with other assessment tools like the SSDF and CAF.

SLSA is inspired by Google's internal Binary Authorization for Borg a mandatory enforcement check for all of Google's production workloads.

Software Delivery Shield is a fully-managed software supply chain security solution on Google Cloud that incorporates best practices in SLSA. You can view insights about your security posture, including the SLSA level of your builds.

Artifact and dependency management
Visibility into vulnerabilities in your software lets you proactively respond and remediate potential threats before you release your applications to your customers. You can use the following tools to get more visibility into vulnerabilities.

Vulnerability scanning
Vulnerability scanning services such as Artifact Analysis help you to identify known vulnerabilities in your software.
Dependency management
Open Source Insights is a centralized source for information about dependency graphs, known vulnerabilities, and licenses associated with open source software. Use the site to learn about your dependencies.

The Open Source Insights project also makes this data available as an Google Cloud Dataset. You can use BigQuery to explore and analyze the data.

Source control policy
Scorecards is an automated tool that identifies risky software supply chain practices in your GitHub projects.

Allstar is a GitHub App that continuously monitors GitHub organizations or repositories for adherence to configured policies. For example, you can apply a policy to your GitHub organization that checks for collaborators outside the organization who have administrator or push access.

To learn more about managing your dependencies, see Dependency management

Team awareness about cybersecurity
If your teams have an understanding of software supply chain threats and best practices, they can design and develop more secure applications.

In the State of Cybersecurity 2021, Part 2, a survey of information security professionals, survey respondants reported that cybersecurity training and awareness programs had some positive impact (46%) or strong positive impact (32%) on employee awareness.

The following resources can help you learn more about supply chain security and security on Google Cloud:

Google Cloud enterprise foundation blueprint describes setting up organization structure, authentication and authorization, resource hierarchy, networking, logging, detective controls, and more. It is one of the guides in the Google Cloud security best practices center.
Developing Secure Software teaches foundational software development practices in the context of software supply chain security. The course focuses on best practices for designing, developing, and testing code, but also covers topics such as handling vulnerability disclosures, assurance cases, and considerations for software distribution and deployment. The Open Source Security Foundation (OpenSSF) created the training.
Preparing for change
After you have identified changes you want to make, you need to plan for the changes.

Identify best practices and mitigations to improve the reliability and security of your supply chain.
Develop guidelines and policies to ensure that teams implement changes and measure compliance consistently. For example, your company policies might include criteria for deployment that you implement with Binary Authorization. The following resources can help you:

Minimum Viable Secure Product, a security checklist of controls to establish a baseline security posture for a product. You can use the checklist to establish your minimum security control requirements and to evaluate software by third-party vendors.
NIST Security and Privacy Controls for Information Systems and Organizations publication (SP 800-53).
Plan for incremental changes to reduce the size, complexity, and impact of each change. It also helps the people on your teams to adjust to each change, provide feedback, and apply lessons you've learned to the future changes.

The following resources can help you with planning and implementing change.

ROI of DevOps Transformation is a white paper that describes how to forecast the value of and justify investment in DevOps transformation.

The Google Cloud Application Modernization Program provides holistic, guided assessment, measuring key outcomes (speed and stability and burnout) and identifying the technical, process, and cultural capabilities that improve those outcomes for your organization. See the CAMP announcement blog post for more information about the program.

How to transform provides guidance to help you plan for and implement changes. Fostering a culture that supports incremental, ongoing change leads to more successful change outcomes.

The NIST Secure Software Delivery Framework describes software security practices based on established practices from organizations such as The Software Alliance, Open Web Application Security Project, and SAFECode. It includes a set of practices to prepare your organization as well as practices for implementing changes and responding to vulnerabilities.
