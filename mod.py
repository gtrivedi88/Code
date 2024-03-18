== Understanding SBOM

{ProductShortName} leverages {RHTPALongName} ({RHTPAShortName}) and its security checks within the pipeline. If {RHTPAShortName} is installed and configured, the pipeline runs the {RHTPAShortName} tasks (for example, `show-sbom`) and displays a green check upon completion. However, if {RHTPAShortName} is not installed or configured, pipeline skips the {RHTPAShortName} tasks.

[NOTE]
====
* {RHTPAShortName} tasks in the pipeline succeed only if you already have installed and configured {RHTPAShortName} as part of the {RHTPAShortName} installation process. For detailed instructions on installing {RHACSShortName}, refer link:{linkRHACSInstallGuide}[Installing Red Hat {RHACSLongName} for Kubernetes].

* If you did not install and configure {RHACSShortName} during the {ProductShortName} installation process, refer link:https://access.redhat.com/documentation/en-us/red_hat_trusted_profile_analyzer/2023-q4/html/quick_start_guide/index[Quick Start] guide.
====

The `show-sbom` task contributes to software supply chain transparency by listing all software libraries a component uses, facilitating the identification of vulnerabilities and assessment of security impacts.
