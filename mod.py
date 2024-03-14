:_mod-docs-content-type: PROCEDURE

[id="view-security-insights_{context}"]
= View security insights

After updating your component, the `on-push` pipeline is automatically triggered. By default, {ProductShortName} uses a standard build pipeline for quick, containerized deployment, enhancing supply chain security by meeting SLSA Build Level 3 specifications.


.A successful pipeline run
image::pipeline_run.png[]

This visual representation outlines each pipeline task. A *green* status indicates successful completion, streamlining your workflow without extensive oversight.

Initial build pipeline tasks include:

* *`init`*: Initializes the pipeline, setting up rebuild flags and authentication. Creates an image repository secret for PipelineRun.

* *`clone-repository`*: Clones the specified repository into the output workspace using the git-clone Task.

* *`build-container`*: Builds the source code into a container image and pushes it to a registry with Buildah. Also generates an SBOM, injects it into the final image, and pushes the SBOM as a separate image with Cosign.

* *`update-deployment`*: Task to update deployment with newly built image in gitops repository.

* *`acs` tasks*: Performs security checks on the code and deployment configurations to ensure adherence to security policies and best practices.

* *`show-sbom`*: Generates a detailed inventory of all software components and libraries used in the application, enhancing transparency and aiding in vulnerability management.

* *`summary`*: Summary Pipeline Task. Prints PipelineRun information, removes image repository secret used by the PipelineRun.

== cs` tasks
If you have installed ACS, the status of the ACS tasks (for example, `roxctl image scan`) appears green. Otherwise, it appears greyed out.


.The ACS tasks in the pipeline run
image::acs-tasks.png[]

The pipeline incorporates three ACS tasks using `roxctl` to perform comprehensive security checks:

* `roxctl image scan` - Scans the code for vulnerabilities

* `roxctl image check` - Scans the code for policy check. For example, 'No log4j allowed' or perhaps no curl, wget nor a package manager in a production image.

* `roxctl deployment check` - Scans the `deployment.yaml` to  identify that your Deployment.yaml has not properly configured its resource request and limit.

These tasks ensure adherence to security policies and configurations right from the development stage.

[discrete]
== Visualizing ACS scan reports

In Red Hat Developer Hub, under the *CI* tab, the Pipeline Runs section offers a feature to access and interpret detailed task reports through a structured pop-up interface. The pop-up consists of the following sections:

* *Advanced Cluster Security (conditionally shown on the availability of ACS tasks):* This section displays the individual tabs all the ACS scan tasks, for example, Image scan, Image check, and Deployment check, and offers an initial summary of the security issues.

* *Others:* This section displays the results of a `PipelineRun`, for example, IMAGE_URL, and `IMAGE_DIGEST`. This section displays only when there is more than one section (for example, Enterprise Contract or Advanced Cluster Security) available in the pop-up.

To view ACS scan reports:

. Select *Catalog* and open an appropriate component for which you want to review the ACS scan reports
. Select the *CI* tab > *Actions* column > *View output* icon and review the detailed ACS scan reports in the software components.

+
.The detailed ACS scan reports
image::acs-report.png[]

[discrete]
== Interpreting ACS scan reports

The detailed reports generated by Advanced Cluster Security (ACS) tasks are instrumental in providing security insights crucial for maintaining a robust security posture.

Here's how to interpret these reports:

* *Vulnerability Breakdown:* ACS scans categorize detected vulnerabilities by severity (Critical, Important, Moderate, Low), status (fixable, non-fixable), and offer a summary of the scan results. This categorization includes the total number of vulnerabilities and components analyzed, alongside specific Common Vulnerabilities and Exposures (CVEs) identified.

* *Details Provided:* For each identified vulnerability, the report includes:

** *CVE ID:* A unique identifier for the vulnerability.
** *Severity:* The level of threat posed by the vulnerability.
** *Component:* The software component affected by the vulnerability.
** *Component Version:* The version of the affected component.
** *Remediation Suggestions:* Recommendations for addressing the vulnerability, including the version in which the vulnerability is fixed, if applicable.

== `show-sbom`
The `scan-export-sbom` task contributes to software supply chain transparency by listing all software libraries a component uses, facilitating the identification of vulnerabilities and assessment of security impacts.

.The `scan-export-sbom` task in the pipeline run
image::sbom-export.png[]

The task pushes the SBOM to a CycloneDX repository for easier access and utilization outside of the CI process.

[NOTE]
====
- If you have installed TPA, the status of the `scan-export-sbom` task appears green. Otherwise, it appears greyed out.

- {ProductShortName} does not support CycloneDX.
====

[discrete]
== Viewing SBOM

You can use an SBOM to better understand the composition of your software, identify vulnerabilities, and assess the potential impact of any security issues that might arise.

.Procedure

. Select *Catalog* and open an appropriate component for which you want to view SBOM.
. Select the *CI* tab and then select the link icon.

.. If you have defined the external link, selecting link icon displays the SBOM in a new tab.

.. If you have not defined an external link, selecting link icon displays the SBOM task logs and you can use your web browser to immediately search the SBOM for terms that indicate vulnerabilities in your software supply chain. For example, try searching for `log4j`.

[discrete]
== Reading the SBOM

In the SBOM, as the following sample excerpt shows, you can see four characteristics of each library that a project uses:

* Its author or publisher

* Its name

* Its version

* Its licenses

This information helps you verify that individual libraries are safely-sourced, updated, and compliant.

.Example SBOM

[source,json]
----
{
   "bomFormat": "CycloneDX",
   "specVersion": "1.4",
   "serialNumber": "urn:uuid:89146fc4-342f-496b-9cc9-07a6a1554220",
   "version": 1,
   "metadata": {
       ...
   },
   "components": [
       {
           "bom-ref": "pkg:pypi/flask@2.1.0?package-id=d6ad7ed5aac04a8",
           "type": "library",
           "author": "Armin Ronacher <armin.ronacher@active-4.com>",
           "name": "Flask",
           "version": "2.1.0",
           "licenses": [
               {
                   "license": {
                       "id": "BSD-3-Clause"
                   }
               }
           ],
           "cpe": "cpe:2.3:a:armin-ronacher:python-Flask:2.1.0:*:*:*:*:*:*:*",
           "purl": "pkg:pypi/Flask@2.1.0",
           "properties": [
               {
                   "name": "syft:package:foundBy",
                   "value": "python-package-cataloger"
                   ...
----


= View Security Insights

After updating your component, the `on-push` pipeline is automatically triggered. By default, {ProductShortName} uses a standard build pipeline for quick, containerized deployment, enhancing supply chain security by meeting SLSA Build Level 3 specifications.

.A Successful Pipeline Run
image::pipeline_run.png[]

This visual representation outlines each pipeline task. A "green" status indicates successful completion, streamlining your workflow without extensive oversight. Key tasks include:

[discrete]
== `init`
Initializes the pipeline, setting up rebuild flags and authentication. Creates an image repository secret for PipelineRun.

[discrete]
== `clone-repository`
Clones the specified repository into the output workspace using the git-clone Task.

[discrete]
== `build-container`
Builds the source code into a container image and pushes it to a registry with Buildah. Also generates an SBOM, injects it into the final image, and pushes the SBOM as a separate image with Cosign.

[discrete]
== `acs` tasks
[NOTE]
====
ACS tasks like `roxctl image scan` show as green if ACS is installed, otherwise greyed out.
====
.The ACS Tasks in the Pipeline Run
image::acs-tasks.png[]

Three ACS tasks perform security checks:

* `roxctl image scan` - Scans for vulnerabilities.
* `roxctl image check` - Enforces policy checks, e.g., banning log4j.
* `roxctl deployment check` - Verifies `deployment.yaml` configurations.

[discrete]
== Visualizing ACS Scan Reports

Access detailed task reports via a structured pop-up in the Red Hat Developer Hub under the *CI* tab. The pop-up includes:

* *Advanced Cluster Security*: Shows tabs for ACS tasks with summaries of identified security issues.
* *Others*: Displays results like IMAGE_URL and IMAGE_DIGEST, visible when additional sections are present.

.Viewing ACS Scan Reports
Procedure:

. In *Catalog*, select the component to review ACS scan reports.
. In the *CI* tab, under *Actions*, click the *View output* icon.

.The Detailed ACS Scan Reports
image::acs-report.png[]

[discrete]
== Interpreting ACS Scan Reports

Reports provide crucial security insights:

* *Vulnerability Breakdown*: Categorizes vulnerabilities by severity and fixability.
* Each vulnerability report includes CVE ID, severity, affected component, version, and remediation suggestions.

[Discrete]
== `show-sbom`
Pushes SBOM to a CycloneDX repository, enhancing transparency.

.The `scan-export-sbom` Task
image::sbom-export.png[]

[NOTE]
====
- Green status appears for `scan-export-sbom` if TPA is installed.
- {ProductShortName} does not support CycloneDX directly.
====

[discrete]
== Viewing SBOM

SBOMs detail software composition, aiding in vulnerability identification.

.Procedure

. In *Catalog*, open the component for SBOM review.
. In the *CI* tab, click the link icon.

.. External links open the SBOM in a new tab.
.. Absence of an external link shows the SBOM task logs for direct search.

[discrete]
== Reading the SBOM

SBOMs list project-used libraries, including author, name, version, and licenses.

.Example SBOM
[source,json]
----
{
   "bomFormat": "CycloneDX",
   "specVersion": "1.4",
   "serialNumber": "urn:uuid:89146fc4-342f-496b-9cc9-07a6a1554220",
   "version": 1,
   "metadata": {
       ...
   },
   "components": [
       {
           "bom-ref": "pkg:pypi/flask@2.1.0",
           "type": "library",
           "author": "Armin Ronacher",
           "name": "Flask",
           "version": "2.1.0",
           "licenses": [{"license": {"id": "BSD-3-Clause"}}],
           "cpe": "cpe:2.3:a:flask:2.1.0",
           "purl": "pkg:pypi/Flask@2.1.0",
           "properties": [{"name": "foundBy", "value": "python-package-cataloger"}]
           ...
----
