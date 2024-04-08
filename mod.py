== Unregister or remove your application

. Navigate to the *Catalog* and select the component that you want to unregister or remove.

. Select vertical three-dot menu associated with the component, and then select *Unregister entity*. A confirmation dialog appears.

+
image::unregister.png[]

. Select *Unregister Location*.

. Navigate to the *Catalog*, from *Kind* drop-down list select *Resource*, and then unregister the corresponding GitOps resource.

[]
----
Unregistering removes the component from your view but it does not delete the application from the cluster.
----

. To remove the running component from the cluster, run the following command:

[source,bash]
----
oc delete application your-app-name-app-of-apps -n rhtap # <1>
----
<1> `rhtap` is the default namespace.

. (Optional) To remove the permanently component from the catalog, on the confirmation dialog, select *Advanced* and then select *Delete Entity*.

+
[NOTE]
----
This should only be done if you know that the catalog file has been deleted at, or moved from, its origin location. If that is not the case, the entity will reappear shortly as the next refresh round is performed by the catalog.
----
