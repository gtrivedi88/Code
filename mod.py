Narrator: One of the biggest challenges with onboarding a new hire or even simply moving a developer from one team to another is that each codebase often has unique standards.

You might have heard the phrase "golden path template" and if you were in the Netherlands you might call this concept the "kings road". The idea is fairly simple though I have to admit it is a challenge to implement. All the corporate standards can be embodied as code. You might hear this theme a fair bit "as code" and everything stored in a git repository.

The core idea of a golden path template is that it is the well worn, well supported path to production. If the developer stays on the path then their app easily lands in production. Remember code offers no business value until it lands in production.

Note: the templates here will be customized by each organization but we want to show you one with some interesting supply chain security capabilities. In addition, how a template provisions infrastructure will be unique per organization. In this demo case, the template leverages ArgoCD aka OpenShift GitOps to dynamically provision OpenShift resources like Namespaces and secrets.
