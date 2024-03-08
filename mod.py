CHAPTER 1. OVERVIEW OF GENERAL CONCEPTS IN RHTAP
With Red Hat Trusted Application Pipeline you can assess and elevate your organization’s security defense. Assess and Elevate represents a proactive, two-phased approach aimed at fortifying cybersecurity within the software development lifecycle (SDLC). This methodology begins with a comprehensive evaluation of existing security measures across all development stages. Upon completing this initial assessment, the focus shifts towards enhancing these practices. This is achieved by integrating advanced security solutions and adopting a DevSecOps CI/CD solution, which standardizes developer onboarding, accelerates processes, and embeds security measures from the outset.

1.1. {PRODUCT}: A COMPREHENSIVE FRAMEWORK FOR SECURE CI/CD
ProductName} (RHTAP) serves as a holistic solution for building, testing, and deploying source code within a secure CI/CD environment. Adhering to SLSA level 3 best practices, RHTAP is instrumental in identifying critical vulnerabilities early on.

1.2. DEEP DIVE INTO RHTAP'S SECURITY TOOLS
Ensuring the security of software throughout its development is essential for mitigating potential vulnerabilities. The RHTAP leverages a powerful suite of tools designed to bolster your security measures. Let’s explore how RHTAP utilizes its components — RHDH, RHTAS, and RHTPA — to provide a robust defense against security threats.

Red Hat Developer Hub (RHDH) Red Hat Developer Hub serves as a self-service portal for developers. It streamlines the onboarding process and offers access to a wealth of resources and tools necessary for secure software development. This platform encourages best practices and facilitates the integration of security measures right from the start of the development process.

Red Hat Trusted Artifact Signer (RHTAS) Red Hat Trusted Artifact Signer focuses on enhancing software integrity through signature and attestation mechanisms. By ensuring that every piece of code and every artifact is signed and attested, RHTAS provides a verifiable trust chain that confirms the authenticity and security of the software components being used.

Red Hat Trusted Profile Analyzer (RHTPA) Red Hat Trusted Profile Analyzer, deals with the generation and management of Software Bills of Materials (SBOMs). SBOMs are critical for maintaining transparency and compliance, as they provide a detailed list of all components, libraries, and dependencies included in a software product. RHTPA automates the creation of SBOMs, ensuring that stakeholders have accurate and up-to-date information on the software’s composition.

1.3. ENHANCING SECURITY WITH KEY PRACTICES
RHTAP incorporates these tools to address specific security concerns effectively:

Vulnerability Scanning: With each pull request, RHTAP conducts thorough scans to identify and address vulnerabilities at the earliest possible stage. This proactive approach ensures that potential security issues are resolved before they can impact the broader system.
SBOM Generation: RHTAP’s automated generation of SBOMs plays a vital role in maintaining software transparency and compliance. By providing a comprehensive inventory of software components, organizations can better manage and secure their software supply chain.
Container Image Security: RHTAP verifies that container images comply with SLSA (Supply-chain Levels for Software Artifacts) guidelines. This is achieved through an enterprise contract that includes over 41 rules, ensuring that the container images used in the development process meet stringent security standards.
By integrating RHDH, RHTAS, and RHTPA into the software development lifecycle, RHTAP provides a comprehensive framework for enhancing security measures. This holistic approach not only safeguards against current threats but also lays a solid foundation for responding to future challenges in cybersecurity.

1.4. EMBRACING SHIFT-LEFT AND SHIFT-DOWN SECURITY PRACTICES
Shift-left and shift-down strategies underscore the importance of integrating security measures early in the SDLC. Introducing security checks at the code entry point and embedding security practices from the project’s inception guarantees a more secure development process.

1.5. LEVERAGING READY-TO-USE SOFTWARE TEMPLATES
RHTAP’s ready-to-use software templates offer predefined pathways that incorporate security practices directly into the development workflow. These templates significantly reduce the cognitive load on developers, enabling them to concentrate more on innovation and less on security-related concerns.

Note
The ready-to-use software templates are customizable to meet your organization’s specific requirements.

1.6. THE PATH FORWARD
Embracing a DevSecOps mindset and utilizing RHTAP promotes a secure and efficient development environment. This ongoing journey of assessment and elevation equips organizations to address both current and future cybersecurity challenges effectively.

Next steps

To learn about RHTAP, see <link to Jocelyn’s doc>
Exploring secure supply chain elements in your build pipeline
Additional resources

For information on Red Hat Developer Hub, see Getting started with Red Hat Developer Hub guide.
For information on Red Hat Trusted Artifact Signer, see {RHTAShortName} Deployment guide.
For information on Red Hat Trusted Profile Analyzer, see Quick Start guide.
