 In the *Deployment Namespace* field, enter the namespace or cluster where your application will be deployed to.
 In the *Deployment Namespace* field, enter the namespace or cluster where your application will be deployed to.
it does not need to be exist any more. The app-of-apps structure can handle the namespace creation.
but you may want to mention the field here is for namespace prefix. so the actual namespaces will be created are `<prefix>-development`, `<prefix>-stage` and `<prefix>-prod`. I will also update the UI to note that
