:_mod-docs-content-type: CONCEPT

[id="understanding-rhtap-foundations_{context}"]
= Understanding {ProductShortName}'s foundations

{ProductName} ({ProductShortName}) implements a strategic approach to enhance cybersecurity throughout the software development lifecycle (SDLC). This approach focuses on identifying and addressing vulnerabilities during coding, building, running, and deployment phases. It starts with detailed assessment of current security practices, followed by advancements through the integration of cutting-edge security solutions and a DevSecOps CI/CD framework. This strategic approach ensures streamlined developer onboarding, process acceleration, and the embedding of security from the beginning.

== Secure CI/CD Framework

{ProductShortName} is a comprehensive framework designed for the secure building, testing, and deploying of source code. By adhering to Supply-chain Levels for link:https://slsa.dev/spec/v1.0/levels[Software Artifacts (SLSA) level 3] best practices with our sample Tekton build pipelines, {ProductShortName} plays a crucial role in the early detection of vulnerabilities.

== Deep dive into {ProductShortName}'s security tools

Ensuring the security of software throughout its development is essential for mitigating potential vulnerabilities. The {ProductShortName} leverages a powerful suite of tools designed to bolster your security measures. Let’s explore how {ProductShortName} utilizes its components — {RHDHShortName}, {RHTASShortName}, and {RHTPAShortName} — to provide a robust defense against security threats.

*{RHDHLongName} ({RHDHShortName})*

* {RHDHLongName} serves as a self-service portal for developers. It streamlines the onboarding process and offers access to a wealth of resources and tools necessary for secure software development. This platform encourages best practices and facilitates the integration of security measures right from the start of the development process.

*{RHTPALongName} ({RHTASShortName})*

* {RHTPALongName} focuses on enhancing software integrity through signature and attestation mechanisms. By ensuring that every piece of code and every artifact is signed and attested, {RHTASShortName} provides a verifiable trust chain that confirms the authenticity and security of the software components being used.

*{RHTPALongName} ({RHTPAShortName})*

* {RHTPALongName}, deals with the generation and management of Software Bills of Materials (SBOMs). SBOMs are critical for maintaining transparency and compliance, as they provide a detailed list of all components, libraries, and dependencies included in a software product. {RHTPAShortName} automates the creation of SBOMs, ensuring that stakeholders have accurate and up-to-date information on the software’s composition.

== Leveraging ready-to-use software templates

{ProductShortName}’s ready-to-use software templates offer predefined pathways that incorporate security practices directly into the development workflow. These templates significantly reduce the cognitive load on developers, enabling them to concentrate more on innovation and less on security-related concerns.

[NOTE]
====
You can customize the ready-to-use software templates to meet your organization’s specific requirements.
====

The ready to use software templates come with default integrate:
* ACS: Add details
* Quay: Add details
* Pipelines: Add details and talk about pipeline as code
* GitOps: Add details


== Key security practices

{ProductShortName} incorporates these tools to address specific security concerns effectively:

* *Vulnerability Scanning:* With each pull request, {ProductShortName} conducts thorough scans with your CVE scanner of choice, such as Advanced Cluster Security, to identify and address vulnerabilities at the earliest possible stage.

* *SBOM Generation:* {ProductShortName}’s automated generation of SBOMs plays a vital role in maintaining software transparency and compliance. By providing a comprehensive inventory of software components, organizations can better manage and secure their software supply chain.

* *Container Image Security:* {ProductShortName} verifies that container images comply with link:https://slsa.dev/[SLSA (Supply-chain Levels for Software Artifacts)] guidelines. This is achieved through an enterprise contract that includes over 41 rules, ensuring that the container images used in the development process meet stringent security standards.

== The path forward

Embracing a DevSecOps mindset and utilizing {ProductShortName} promotes a secure and efficient development environment. This ongoing journey of assessment and elevation equips organizations to address both current and future cybersecurity challenges effectively.

[role="_additional-resources"]
.Next steps

* xref:installing-red-hat-trusted-application-pipeline_{context}[Install {ProductName}]


[role="_additional-resources"]
.Additional resources

* For information on {RHDHLongName}, see link:https://access.redhat.com/documentation/en-us/red_hat_developer_hub/1.0/html/getting_started_with_red_hat_developer_hub/index[Getting started with {RHDHLongName} guide].

* For information on {RHTPALongName}, see {RHTASShortName} link:https://access.redhat.com/documentation/en-us/red_hat_trusted_artifact_signer/2024-q1/html/deployment_guide/index[Deployment] guide.

* For information on {RHTPALongName}, see link:https://access.redhat.com/documentation/en-us/red_hat_trusted_profile_analyzer/2023-q4/html/quick_start_guide/index[Quick Start] guide.
