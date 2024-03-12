The build-sign-image phase integrates Tekton Chains to strengthen supply chain security in OpenShift Pipelines. By signing task runs and utilizing attestation formats such as in-toto, Tekton Chains elevates trust and security throughout the development process.

<image>

The PipelineRun displays the signed badge next to its name only if you have configured Tekton Chains. For information on configuring Tekton Chains, see link:https://docs.openshift.com/pipelines/1.13/secure/using-tekton-chains-for-openshift-pipelines-supply-chain-security.html[Using Tekton Chains for OpenShift Pipelines supply chain security].


Additionally, you can select the Image Registry tab to review. In the Image Registry tab, artifacts such as `.att` (attestations), `.sig` (signatures), and `.sbom` (Software Build of Materials) files are stored alongside the container image, further reinforcing the security of your application.
