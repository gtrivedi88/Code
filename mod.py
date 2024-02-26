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
The image scan, image check, and deployment check tasks in the Advanced Culster Security (ACS) provides a crucial analysis of vulnerabilities within the container images. 
To view the scan task report:
In the OpenShift Pipeline interface, select the Pipeline Run you wish to analyze.
Click the "CI" tab and locate the "View Output" icon in the Actions column.
Select the "Image Scan" tab in the pop-up window that appears.


Understanding the Report Contents
The Image Scan report is divided into several key areas:
CVEs by Severity: This area categorizes the Common Vulnerabilities and Exposures (CVEs) found in the image by their severity levels—Critical, Important, and Low. Critical vulnerabilities demand immediate attention, while lower-severity issues may be prioritized accordingly.
CVEs by Status: It provides a split view of vulnerabilities with available fixes and those without, enabling you to quickly understand which issues can be readily addressed.
Total Scan Results: This gives a summary of the scan, including the total number of vulnerabilities and components analyzed.


Detailed Vulnerability Information
Each entry in the image scan report includes:
CVE ID: A unique identifier for the vulnerability. Clicking on the CVE ID link will redirect to an external database for in-depth information.
Severity: The assigned severity level based on the potential impact of the vulnerability.
Component: The software component where the vulnerability was found.
Component Version: The version of the component that was scanned.
Fixed in Version: If available, the version in which the vulnerability has been addressed is listed.


Each entry in the image check and deployment check report includes:
Name
Severity
Break build
Description
Violation
Remediation


Using Filters
For the image scan task, you can filter the report by:
CVE ID
Severity
Component
Status
Filter by name


For the image check task, you can filter the report by:
Status 
Severity
Filter by name


For the deployment check, you can filter the report by:
Severity
Filter by name




Interpreting the Results
Critical Vulnerabilities: These should be reviewed and addressed as a priority to minimize the risk of exploitation.
Fixable vs. Unfixable: Focus on vulnerabilities that can be fixed with available patches. For unfixable vulnerabilities, consider workarounds or additional security measures.
Remediation Guidance: For each listed vulnerability, assess the 'Fixed in Version' information to plan for component updates or patches.
