:_mod-docs-content-type: CONCEPT

[id="understanding-rhtap-foundations_{context}"]
= Understanding {ProductShortName}'s foundations

Discover the robust foundation of {ProductName} ({ProductShortName}), a platform designed to revolutionize cybersecurity practices across the software development lifecycle (SDLC). With {ProductShortName}, you embark on a journey that transcends traditional security measures, integrating cutting-edge solutions and a DevSecOps CI/CD framework from inception to deployment. This proactive strategy not only accelerates developer onboarding and processes but also embeds ironclad security at every step, safeguarding your projects against emerging threats.


== Secure CI/CD Framework

At the heart of {ProductShortName} lies a secure CI/CD framework that sets new standards in software development. By aligning with the Supply-chain Levels for link:https://slsa.dev/spec/v1.0/levels[Software Artifacts (SLSA) level 3], {ProductShortName} ensures that every line of code contributes to a fortress of security, significantly enhancing early vulnerability detection and mitigation.

== Deep dive into {ProductShortName}'s security tools

Ensuring the security of software throughout its development is essential for mitigating potential vulnerabilities. The {ProductShortName} leverages a powerful suite of tools designed to bolster your security measures. Let’s explore how {ProductShortName} utilizes its components — {RHDHShortName}, {RHTASShortName}, and {RHTPAShortName} — to provide a robust defense against security threats.

*{RHDHLongName} ({RHDHShortName})*

* {RHDHLongName} serves as a self-service portal for developers. It streamlines the onboarding process and offers access to a wealth of resources and tools necessary for secure software development. This platform encourages best practices and facilitates the integration of security measures right from the start of the development process.

*{RHTPALongName} ({RHTASShortName})*

* {RHTPALongName} focuses on enhancing software integrity through signature and attestation mechanisms. By ensuring that every piece of code and every artifact is signed and attested, {RHTASShortName} provides a verifiable trust chain that confirms the authenticity and security of the software components being used.

*{RHTPALongName} ({RHTPAShortName})*

* {RHTPALongName}, deals with the generation and management of Software Bills of Materials (SBOMs). SBOMs are critical for maintaining transparency and compliance, as they provide a detailed list of all components, libraries, and dependencies included in a software product. {RHTPAShortName} automates the creation of SBOMs, ensuring that stakeholders have accurate and up-to-date information on the software’s composition.

== Leveraging ready-to-use software templates

Imagine focusing solely on innovation, unencumbered by security concerns. {ProductShortName}'s ready-to-use software templates make this a reality, embedding security seamlessly into your development workflow and significantly lightening the cognitive load for your developers.

[NOTE]
====
Flexibility at its finest: tailor these ready-to-use software templates to precisely fit your organization's needs.
====

Benefit from integrated features right out of the box:

* *ACS:* Advanced Container Security to fortify your deployments.

* *Quay:* A secure harbor for your container registries.

* *Tekton pipelines:* Automate your deployments with precision.

* *GitOps:* Maintain consistency and automate configuration management with ease.

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
