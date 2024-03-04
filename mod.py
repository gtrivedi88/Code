This pipeline has a special task called verify-enterprise-contract

Enterprise Contract (EC) is a special CLI that compliments Sigstore’s cosign. If you remember the build-sign-image task that produced and stored the .sig and .att artifacts into the container registry, EC evaluates that signature and attestation. EC is based on the rego policy language from Open Policy Agent and allows you to create custom rules to review cosign attest attestations. By default, EC works with the SLSA provence attestation coming out of Tekton Chains.

Enterprise Contract, as part of this promotion pipeline, is verifing that the container image did in fact come from the corporate standard/approved build system. In other words, this container image was not built on some random person’s laptop, it was built in the secure build system. The .att, .sbom and .sig are stored alongside the container image and a tool like skopeo can be used to move all items together.

https://enterprisecontract.dev/
