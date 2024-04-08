In the catalog goto to the app and select the menu at top right, and "unregister" it  - this unregisters the git repo for that app
You also need to unregister the gitops app which is in "Resources" ... Evertything is still running, it does nothing to your cluster
To remove the running stuff you can remove the app-of-apps  oc delete application your-app-name-app-of-apps -n rhtap 
