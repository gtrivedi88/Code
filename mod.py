:_mod-docs-content-type: CONCEPT
[id="con_enterprise-contract-for-rhtap_{context}"]

= {ECShort} for {ProductName}

The more complex a software supply chain becomes, the more critical it is to employ reliable checks and best practices to guarantee software artifact integrity and source code dependability. Artifacts such as your image containers. This is where {ECLong} enters your {ProductName} build and deploy experience.

{ECShort} is a policy-driven workflow tool for maintaining software supply chain security by defining and enforcing policies for building and testing container images. For a build system that creates Supply-chain Levels for Software Artifacts (SLSA) provenance attestations, such as Tekton with Tekton Chains and GitHub Actions with the SLSA GitHub Generator, checking the signatures and confirming that the contents of the attestations actually match what is expected is a critical part of verifying and maintaining the integrity of your software supply chain. A secure CI/CD workflow should include artifact verification to detect problems early. It’s the job of {ECShort} to validate that a container image is signed and attested by a known and trusted build system.

The general steps for validating a signed and attested container image are as follows:

. Create or copy a container image with {ProductName}.
. Generate a signing key with Cosign.
. Sign the container image with Cosign.
. Attest the image with Cosign.
. Verify your signed and attested container image with the {ECShort} CLI.

But what does it mean to _sign_ and _attest to the provenance of_ a software artifact like a container image? Why do it? And how?

Signed software artifacts like container images are at a significantly lower risk of several attack vectors than unsigned artifacts. When a container image is signed, various cryptographic techniques bind the image to a specific entity or organization. The result is a digital signature that verifies the authenticity of the image so that you can trace it back to its creator&mdash;that entity or organization&mdash;and also verify that the image wasn’t altered or tampered with after it was signed. For more information about software supply chain threats, see link:https://slsa.dev/spec/v1.0/threats-overview[Supply chain threats].

{ECShort} uses the industry standard link:https://www.sigstore.dev/[Sigstore] link:https://docs.sigstore.dev/signing/quickstart/[Cosign] as a resource library to validate your container images. With {TASShort}, Red Hat's supported version of the Sigstore framework, you can use your own on-prem instance of Sigstore’s services to sign and attest your container images with the Cosign CLI. For more information about {TASShort}, see link:https://access.redhat.com/documentation/en-us/red_hat_trusted_artifact_signer/1/html/deployment_guide/index[Red Hat Trusted Artifact Signer].

As for software artifact _attestation_, it can’t happen without provenance. _Provenance_ is the verifiable information about software artifacts like container images that describes where, when, and how that artifact was produced. The attestation itself is an authenticated statement, in the form of metadata, that proves that an artifact is intact and trustworthy. {ECShort} uses that attestation to cryptographically verify that the build was not tampered with, and to check the build against any set of policies, such as SLSA requirements. For more information about SLSA, see link:https://slsa.dev/spec/v1.0/about[About SLSA].

When you push your code from either the {ProductShortName} development namespace to the stage namespace, or from the stage namespace to the production namespace, {ECShort} automatically runs its validation checks to make sure your container image was signed and attested by known and trusted build systems. When your image passes the {ECShort} check, you can merge your code changes to complete your promotion from one environment to the next. For more information about deploying your application to a different namespace, see link:https://github.com/redhat-appstudio/tssc-sample-templates/blob/main/skeleton/backstage/docs/index.md[Trusted Application Pipeline Software Template]. For more inforamtion about where {ProductShortName} saves your deployment manifests, see the link:https://github.com/redhat-appstudio/build-definitions/tree/main/pipelines/gitops-pull-request-rhtap[{ProductShortName} GitOps repository] and its YAML files.


[role="_additional-resources"]
.Additional resources

For more information about signing and attesting a container image, see link:https://access.redhat.com/documentation/en-us/red_hat_trusted_application_pipeline/1.0/html-single/managing_compliance_with_enterprise_contract/index#proc_signing-container-image_enterprise_contract-rhtap[Signing a container image].


