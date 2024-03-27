. (Optional) If you want to change the deployment namespace prefix post-installation:

.. Log in to the OpenShift web console with your administrator credentials.

.. Create create three namespaces with the suffixes `-development` , `-prod`, and `-stage`.

.. Locate the `rhtap` project. Pipelines associated with this project are listed here.

.. Identify the pipeline named `dev_namespace_setup`.

.. For newly created namespaces (for example, `<your-application>-development` , `<your-application>-prod`, and `<your-application>-stage`)

... Select the *...* menu for the `dev_namespace_setup` pipeline.

... Select *Start Pipeline*.

... In the *Namespace* dropdown, choose the corresponding namespace you want to run the pipeline in (for example, `<your-application>-development`)

... Select *Start*.

... Repeat steps 5a through 5e for each namespace to execute the `dev_namespace_setup` pipeline.


oc new-project "$PREFIX-development"
oc new-project "$PREFIX-stage"
oc new-project "$PREFIX-prod"
