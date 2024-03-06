:_mod-docs-content-type: PROCEDURE
[id="setting-up-openshift-pipelines-to-view-detailed-vulnerability-scan-reports_{context}"]

= Setting up OpenShift Pipelines to view detailed task reports

In Red Hat Developer Hub, under the CI tab, the Pipeline Runs section offers a feature to access and interpret detailed task reports through a structured pop-ip interface. The pop-up window consists of the following sections:

* *Others:* This section displays the results of a PipelineRun, for example, IMAGE_URL, or `IMAGE_DIGEST`, which give context and references for the vulnerabilities scan.

* *(Optional) Advanced Cluster Security:* If you have used Advanced Cluster Security (ACS) scan tasks in your pipeline, this section displays the individual tabs all the ACS scan tasks, for example, Image scan, Image check, and 
Deployment check, and offers an initial summary of the security issues.

* *(Optional) Enterprise Contract:* If you have used Enterprise Contract (EC) scan tasks in your pipeline, this section displays information regarding your application's compliance with the Supply chain Levels for Software Artifacts (SLSA) security framework. n Enterprise Contract is a tool that verifies the provenance of application snapshots against a defined policy, ensuring compliance with the Supply chain Levels for Software Artifacts (SLSA) security framework. Developers can refer to the Enterprise Contract within their workspace to confirm the build’s integrity and adherence to specified requirements.

== Setting up OpenShift Pipelines to view detailed ACS scan reports

It's important to know that this is just an example of vulnerability scan task using `roxctl`. `roxctl` is a community-driven project and is not supported by Red Hat Developer Hub by default.  


.Prerequisites

* You have link:https://docs.openshift.com/container-platform/4.14/web_console/web-console.html#web-console[logged in to the web console].

* You have the appropriate link:https://docs.openshift.com/container-platform/4.14/authentication/using-rbac.html#default-roles_using-rbac[roles and permissions] in a project to create applications and other workloads in OpenShift Container Platform.

* You have an existing vulnerability scan task.

.Procedure

. In the *Developer* or *Administrator* perspective, switch to the relevant project where you want access and interpret detailed vulnerability scan reports

. Update your existing vulnerability scan task with annotations for image scanning, image checking, and deployment checking. For example, when using ACS scanning tool, you can specify annotations for acs-image-scan in the following format:

+
[source,yaml]
----
...
metadata:
 name: acs-image-scan <1>
 annotations:
    task.results.format: application/json <2>
    task.results.type: roxctl-image-scan <3>
    task.results.key: SCAN_OUTPUT
    task.output.location: logs
    task.results.container: step-report <4>
spec: …
      steps:
        - name: report
          image: 'quay.io/lrangine/crda-maven:11.0' <5>
          script: |
              #!/bin/sh
              cat $(workspaces.reports.path)/image-scan
----
<1> Task name. For example, acs-image-scan, acs-image-check, acs-deployment-check
<2> The supported result format
<3> Type of scan tool. For example, `roxctl-image-scan`, `roxctl-image-check`, `roxctl-deployment-check`.
<4> The name of the container to get the POD logs.
<5> The URL of the image to scan.

. Repeat Step 2 for `acs-image-check `and `acs-deployment-check` with appropriate modifications. 

. Rerun the affected OpenShift Pipeline.


.Verification

. Log in to Red Hat Developer Hub.
. Select *Catalog* and open an appropriate project for which you updated the pipeline in Openshift console.
. Select the *CI* tab > *Actions* column > *View output* icon and review the detailed vulnerabilities reports in the software components.


=== Understanding the Vulnerability Report

The image scan, image check, and deployment check tasks in the Advanced Culster Security (ACS) provides a crucial analysis of vulnerabilities within the container images. 

The Image Scan report is divided into several key areas:

* *CVEs by Severity:* This area categorizes the Common Vulnerabilities and Exposures (CVEs) found in the image by their severity levels—Critical, Important, and Low. Critical vulnerabilities might demand immediate attention, while lower-severity issues might be prioritized accordingly.

* *CVEs by Status:* It provides a split view of vulnerabilities with available fixes and those without, enabling you to quickly understand which issues can be readily addressed.

* *Total Scan Results:* This gives a summary of the scan, including the total number of vulnerabilities and components analyzed.

[NOTE]
====
Use filters in the Image scan, Image check, and Deployment check reports to streamline the examination process.
====




=== Detailed Vulnerability Information
Each entry in the image scan report includes:

* *CVE ID:* A unique identifier for the vulnerability. Selecting a CVE ID link, redirects to an external database for for detailed vulnerability information.

* *Severity:* The assigned severity level based on the potential impact of the vulnerability.

* *Component:* The software component where the vulnerability was found.

* *Component Version:* The version of the component that was scanned.

* *Fixed in Version:* If available, the version in which the vulnerability has been addressed is listed.


Each entry in the image check and deployment check report includes:

* *Name:* Indicates the identifier for the vulnerability or check.

* *Severity:* Indicates the assigned risk level.

* *Break build:* Indicates if the build was stopped by a task in the pipeline.

* *Description:* Indicates the nature of vulnerability.

* *Violation:*  Indicates the policy or standard the pipeline run breached.

* *Remediation:* Suggests the steps to address the vulnerability.


=== Interpreting the Results

* *Critical Vulnerabilities:* These should be reviewed and addressed as a priority to minimize the risk of exploitation.

* *Fixable vs. Unavailable:* Focus on vulnerabilities that can be fixed with available patches. For unfixable vulnerabilities, consider workarounds or additional security measures.

* *Remediation Guidance:* For each listed vulnerability, assess the 'Fixed in Version' information to plan for component updates or patches.


== Setting up OpenShift Pipelines to view view Enterprise contract policies reports

It's important to know that the `enterprise contract` is a community project and is not supported by Red Hat Developer Hub by default.  

.Prerequisites

* You have link:https://docs.openshift.com/container-platform/4.14/web_console/web-console.html#web-console[logged in to the web console].

* You have the appropriate link:https://docs.openshift.com/container-platform/4.14/authentication/using-rbac.html#default-roles_using-rbac[roles and permissions] in a project to create applications and other workloads in OpenShift Container Platform.

* You have an existing scan task.

.Procedure

. In the *Developer* or *Administrator* perspective, switch to the relevant project that you want to move to a different environment.

. Update your existing scan task with annotations in the following format:

+
[source,yaml]
----
...
metadata:
 name: enterprise-contract-task <1>
 annotations:
    task.results.format: application/json <2>
    task.results.type: ec <3>
    task.output.location: logs
    task.results.container: step-report-json <4>
spec: …
      steps:
        - name: report-json
          image: quay.io/enterprise-contract/ec-cli:snapshot@sha256:33be4031a3316a46db3559a4d8566bc22f9d4d491d262d699614f32f35b45b67 <5>
          command: [cat]
          args:
            - "$(params.HOMEDIR)/report-json.json"
----
<1> Name of the task, such as enterprise-contract-task.
<2> Format supported for the result.
<3> Type of scan tool, here ec.
<4> Container name for retrieving POD logs.
<5> Image URL for the scanning tool.


. Rerun the affected OpenShift Pipeline.


.Verification

. Log in to Red Hat Developer Hub.
. Select *Catalog* and open an appropriate project for which you updated the pipeline in Openshift console.
. Select the *CI* tab > *Actions* column > *View output* icon and review the Enterprise Contract reports for your software components.

+
image::rhdh-plugins-reference/enterprise-pipeline.png[]

. Select the View output icon within the Actions column to open the scan results pop-up.

+
image::rhdh-plugins-reference/enterprise-details.png[]

=== Understanding the Enterprise Contract Policy Report
The pop-up window presents the Enterprise Contract policy report, which includes the following:

* *Summary:* Displays the count of successful checks and any warnings or failures.

* *Rules:* Lists the individual policy rules checked during the pipeline run, such as source code reference and attestation checks.

* *Status and Messages:* Provides the status of each rule (e.g., Success, Warning) and associated messages for any warnings or failures.

[NOTE]
====
Use filters to streamline the policy review process
====

=== Interpreting Policy Compliance

Expand and review each rule to understand the compliance status of your application.
Address any warnings or failures by referring to the provided messages and take the necessary corrective action to ensure compliance.


