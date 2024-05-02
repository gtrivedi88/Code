Bring your own Quay repository to the build pipeline

By default, all pipelines push the images to the `quay.io/redhat-user-workloads` repository. It is not mandatory to use this Quay repo, so if you want to use your own Quay repo to control user permissions, you can do this by updating the `output-image` parameter in the pipelines.

.Procedure

. You will need a secret to push the images to your Quay repo. 

.. Follow Quay's link:https://docs.quay.io/glossary/robot-accounts.html[docs] to create a robot account for your repo.
.. Give push access to your repository to the robot account.
.. Retrieve the `.dockercfg` from the "Docker Configuration" menu on your robot account credentials page.
.. Follow the steps to link:proc_creating-secrets-for-your-builds.adoc[create a secret for your build] and do it as an "Image Pull Secret".

[NOTE] 
====
You need to delete the `"auths": {` and one `}` at the end of the docker config file for the secret to work. Until this https://issues.redhat.com/browse/KFLUXBUGS-1160[bug] is resolved. 
For example, this is how you will get the file from Quay:
[source, json]
----
{
  "auths": {
    "quay.io": {
      "auth": "example",
      "email": "example"
    }
  }
}
----
And this is how you should upload it to Konflux:
[source, json]
----
{
  "quay.io": {
    "auth": "example",
    "email": "example"
  }
}
----
====

[start=2]
. Go to the GitHub repo of your component.
. In each .yaml file in the .tekton directory, under params, locate the param named output-image:
.. Change it to the new repository. For example: `quay.io/my-new-quay-repo/my-app:on-pr-{\{revision}}` for the `pull-request` pipeline, and `quay.io/my-new-quay-repo/my-app:{\{revision}}` for the `push` pipeline. This is a best practice to know which images come from a Pull Request and which don't.
