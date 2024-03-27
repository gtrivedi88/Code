== Installation overview

Before tapping into the vast array of benefits offered by {ProductShortName}, the initial step involves its installation within your organization. The installation of {ProductShortName} is structured around six key procedures:

. Creating a GitHub Application
. Forking the Template Catalog
. Cloning the Install Repository
. Creating a `private-values.yaml` file
. Installing {ProductShortName} on Your selected cluster
. Accessing {ProductShortName}


* ClusterAdmin access to an OpenShift Container Platform (OCP) cluster, through both the CLI and the web console.

* An instance of Red Hat Advanced Cluster Security, as well as the following values from that instance:
** ACS API token. You can follow the instructions for the prerequisites link:https://github.com/redhat-appstudio/tssc-sample-pipelines/blob/main/hack/build/README.md#prerequisits[here] to create an API token.
** ACS central endpoint URL. You can follow the instructions link:https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_security_for_kubernetes/4.1/html/configuring/configure-endpoints#doc-wrapper[here] to configure the endpoint.

* To enable ACS to access private repositories in image registries, ACS will need to be configured for your specific registry
** For Quay.io, under Integrations->Image Integrations select the Quay.io card
** Add your OAUTH  tokens to access your specific Quay.io instance
** Validate the access via the test button. This will ensure if the RHTAP is asked to scan a private image, ACS will have access

* A Quay.io account

* The link:https://helm.sh/docs/intro/install/[Helm] CLI tool

* A link:https://github.com/[GitHub] account
