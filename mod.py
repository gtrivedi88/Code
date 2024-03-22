. Commit and push your updates. 

. Create a pull request (PR). This pull request triggers a promotion pipeline run which validates the changed container images for {ECLong} ({ECShort}) policies. The promotion pipeline run offers a visual representation of all the tasks in a pipeline. A *green* status indicates successful completion. You can review the triggered promotion pipeline in the *CI* tab in {RHDHShortName}.

. Review and merge the PR. This triggers ArgoCD to apply build promotion related change. You can navigate to the *CD* tab to review the ArgoCD history for the latest deployment updates. Various columns display the latest updates, showing the application's (for example, `appname-prod`) current status , deployment details, author, commit message (for example, Promote stage to prod), and the container image promoted to production. 


.Verification

* Navigate to the *Topology* tab to review promotion of your application across appropriate namespaces.
