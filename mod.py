== How does it work?

{ProductName} ({ProductShortName}), empowers you to streamline and secure your entire DevSecOps CI/CD process.  This journey begins within {RHDHLongName}, a self-service portal powered by Backstage. Here, you'll find {ProductName} readily available for installation and configuration. With just a few clicks, you can set up {ProductShortName} for your development team.

*Secure Development from the Onset*

Once {ProductShortName} is installed and configured, developers can leverage pre-built, secure templates within {RHDHLongName}. Simply choose the most appropriate ready-to-use software template for your needs, fill in the details, and create a new application. This creates a dedicated development environment that includes everything you need: a code repository (source code and GitOps repositories), technical documentation, and a continuous integration/continuous delivery (CI/CD) pipeline.

*Automated Security Throughout the Pipeline*

Editing the source code triggers a pipeline run within your application. This pipeline ensures every build artifact is signed and attested for authenticity. It also scans for vulnerabilities in your code and automatically generates Software Bills of Materials (SBOMs). These SBOMs detail all components, libraries, and dependencies included in the container image, providing complete transparency into your application's makeup.

*Review, Refine, and Release*

The pipeline presents any identified vulnerabilities for your review and remediation. You can also review the SBOM to gain a deeper understanding of your application's components. Depending on your promotion workflow, you can also promote your application through development, staging, and finally to production. Each promotion triggers another pipeline run, scanning for vulnerabilities and enforcing your Enterprise Contract (EC). The EC ensures container images meet predefined requirements before release. If an image fails this check, the EC generates a report outlining any issues that need resolution.

This streamlined approach with {ProductShortName} empowers developers to focus on innovation while maintaining the highest security standards throughout the development lifecycle.
