== Advanced Cluster Security (ACS) Tasks
This is how we are using ACS inside RHTAP. For ACS task to be successfull here we expect that you have already installed and configured it during the install RHTAP process. If you diFor more information on ACS, refer ACS docs.

If ACS is installed and configured, the status of the ACS tasks (for example, `roxctl image scan`) appears green. Otherwise, it appears greyed out.

.The ACS tasks in the pipeline run
<image>

The pipeline incorporates three ACS tasks using `roxctl` to perform comprehensive security checks:

* `roxctl image scan` - Returns the components and vulnerabilities found in the image in JSON format

* `roxctl image check` - Checks the build-time violations of your security policies in the image. For example, 'No log4j allowed' or perhaps no curl, wget nor a package manager in a production image.

* `roxctl deployment check` - Checks the build-time and deploy-time violations of your security policies in YAML deployment files.

These tasks ensure adherence to security policies and configurations right from the development stage.
