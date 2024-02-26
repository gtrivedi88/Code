Setting up OpenShift Pipelines to view detailed vulnerability scan reports 
The View output icon in the CI tab > Actions column is designed to provide insights into security vulnerabilities identified during the scans. The details can be accessed through a pop-up that appears upon interaction with this icon. It consists of the following sections:
Vulnerability scan details: This section includes the scanner task name, for example, Advanced Cluster Security and offers an initial summary of the security issues.
Scan results tabs: These tabs categorize the results into specific tasks such as Image scan, Image check, and Deployment check. The `image-check` scans container images and categorizes vulnerabilities as either fixable or unavailable. The `deployment-check` scans container images for deployment configurations and indenfifies security concerns within the deployment environment.
Other information: This section displays the results of a PipelineRun such as IMAGE_URL, `IMAGE_DIGEST`, `CHAINS-GIT_URL`, `CHAINS-GIT_COMMIT`, `SCAN_OUTPUT`, which give context and references for the vulnerabilities scan.
Prerequisites
You have logged in to the web console.
You have the appropriate roles and permissions in a project to create applications and other workloads in OpenShift Container Platform.
You have an existing vulnerability scan task.
Procedures
In the Developer or Administrator perspective, switch to the relevant project where you want a visual representation of SBOMs.
Update your existing vulnerability scan task to include annotations for image scanning, image checking, and deployment checking. For example, when using ACS scanning tool, you can specify annotations for acs-image-scan in the following format:


...
metadata:
 name: acs-image-scan <1>
 annotations:
    task.results.format: application/json
    task.results.type: roxctl-image-scan <2>
    task.results.key: SCAN_OUTPUT
    task.output.location: logs
    task.results.container: step-report
spec: …
      steps:
        - name: report
          image: 'quay.io/lrangine/crda-maven:11.0' <3>
          script: |
              #!/bin/sh
              cat $(workspaces.reports.path)/image-scan
<1> Task name. For example, acs-image-scan, acs-image-check, acs-deployment-check
<2> Type of scan tool. For example, roxctl-image-scan, roxctl-image-check, roxctl-deployment-check.
<3> The URL of the image to scan.


3. Repeat Step 2 for acs-image-check and `acs-deployment-check` with appropriate modifications. 
4. Rerun the affected OpenShift Pipeline.
.Verification
Select the Pipeline Run > CI tab > Actions column > View output icon and review the detailed vulnerabilities detected in the software components.


Navigating the Vulnerability Report
Interacting with CVE IDs
Click on the CVE ID to be redirected to an external database where detailed information about the vulnerability is available.


Filtering and sorting
The report can be filtered by component, status, and severity, helping prioritize issues for remediation.


Component Analysis
Component and versions
Lists all the components of the application, the versions scanned, and the vulnerabilities associated with each component.


Fixed in version
Specified rge software version where each vulnerability has been resolved.


Utilizing the SCAN reults
If you have used the 
Resolving vulnerabilities
