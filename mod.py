+
[cols="1,1"]
|===
|Key |Description

|export GITHUB__DEFAULT__HOST
|Set this to your on-prem GitHub host. Default is `github.com`.

|export GITLAB__DEFAULT__HOST
|Set this to your on-prem GitLab host. Default is `gitlab.com`.

|export QUAY__DEFAULT__HOST
|The default Quay URL correspond to your specific on-prem environment. The default quay host is `quay.io`.

|export DEFAULT__DEPLOYMENT__NAMESPACE__PREFIX
|The namespace prefix for deployments within {ProductShortName}. Default is `rhtap-app`.
a|
NOTE: Update this if you have modified the default `trusted-application-pipeline: namespace` during or after the {ProductShortName} installation process.

|===
