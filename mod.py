. Locate the *properties* file within your project. Update this file for the following

+
[cols="1,1"]
|===
|Key |Value

|export GITHUB__DEFAULT__HOST
|The default GitHub host values that correspond to your specific on-prem environment. The default GitHub host is `github.com`.

|export GITLAB__DEFAULT__HOST
|The default GitLab host values that correspond to your specific on-prem environment. The default GitLab host is `gitlab.com`.

|export QUAY__DEFAULT__HOST
|The default Quay URL correspond to your specific on-prem environment. The default quay host is `quay.io`.

|export DEFAULT__DEPLOYMENT__NAMESPACE__PREFIX
|The default deployment namespace prefix. The default deployment namespace prefix is `rhtap-app`.
|===

+
.The properties file
image::properties.png[]

. Run the *generate.sh* script in your terminal. This action adjusts the software templates, replacing default host values with your specified inputs.

+
[source,terminal]
----
./generate.sh
----

+
.The generate.sh script
image::generate.png[]

. Commit your changes and push them to your repository. This update automatically refreshes the default templates in {RHDHShortName} with your custom values.

. (Optional) If you updated the default deployment namespace prefix:

.. Navigate to your instance of the local cloned {ProductShortName} installer.

.. Open `private-values.yaml` file and navigate to `trusted-application-pipeline:`.

+
[source,yaml]
----
trusted-application-pipeline:
  namespaces:
    - rhtap-app
----

.. Update the value against the `namespace` to the new default deployment namespace prefix.

.. Run the `PipeluneRun` in each namespace.
