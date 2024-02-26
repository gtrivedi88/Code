Setting up OpenShift Pipelines to view detailed vulnerability scan reports 
The View output icon in the CI tab > Actions column provides detailed information about the security vulnerabilities identified during the scan. It consists of the following sections:
Vulnerability scan details: Display the name of the scanner task used, for example, Advanced Cluster Security and offers a snapshot of the identified security issues.
Different tabs for different task results, for example, Image Scan, Image Check, and Deployment Check.
Others:
Prerequisites
You have logged in to the web console.
You have the appropriate roles and permissions in a project to create applications and other workloads in OpenShift Container Platform.
You have an existing vulnerability scan task.
Procedures
In the Developer or Administrator perspective, switch to the relevant project where you want a visual representation of SBOMs.
Update your existing vulnerability scan task to add the `image-scan`, task annotations in the following format:


...
metadata:
 name: acs-image-scan
 annotations:
    task.results.format: application/json
    task.results.type: roxctl-image-scan
    task.results.key: SCAN_OUTPUT
    task.output.location: logs
    task.results.container: step-report
spec: …
      steps:
        - name: report
          image: 'quay.io/lrangine/crda-maven:11.0'
          script: |
              #!/bin/sh
              cat $(workspaces.reports.path)/image-scan


apiVersion: tekton.dev/v1
kind: Task
metadata:
 name: acs-image-check
 annotations:
    task.results.format: application/json
    task.results.type: roxctl-image-check
    task.results.key: SCAN_OUTPUT
    task.output.location: logs
    task.results.container: step-report
spec: …
      steps:
        - name: report
          image: 'quay.io/lrangine/crda-maven:11.0'
          script: |
              #!/bin/sh
              cat $(workspaces.reports.path)/image-check




apiVersion: tekton.dev/v1
kind: Task
metadata:
 name: acs-deployment-check
 annotations:
    task.results.format: application/json
    task.results.type: roxctl-deployment-check
    task.results.key: SCAN_OUTPUT
    task.output.location: logs
    task.results.container: step-report
spec: …
      steps:
        - name: report
          image: 'quay.io/lrangine/crda-maven:11.0'
          script: |
              #!/bin/sh
              cat $(workspaces.reports.path)/deployment-check
Note: If you need additional image checks, you can add all them in the following above format for example, image check, deployment check.
3. Rerun the affected OpenShift Pipeline.
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


Actionable insights
If you have used the 
Resolving vulnerabilities
