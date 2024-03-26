Red Hat Trusted Application Pipeline

Developing an application is a long and multistep process. Add several teams and immense computing power, and now you’ve got an expensive process, too. Even more importantly: Your app is sophisticated. You wouldn’t have expended so much time, money, and power–human and machine–if it wasn’t. Sophisticated apps have complex software supply chains, and the longer a software supply chain is, the more vulnerable it is to attacks of all kinds.


Keep your app and its entire software supply chain safe with {ProductName} ({ProductShortName}). {ProductShortName} can build, test, and deploy your source code with secure CI/CD, and its comprehensive set of security tools keeps your complete software supply chain secure.


Table 1. Key features






Continuously build, test, and deploy container images from your Git source code.
X


Built-in example templates get you learning and customizing right away.
X


Build Java, Python, Node, Go, or npm-based apps into container images.
X


Automatically deploy container images to a built-in development environment.
X


Continuously deploy with GitOps Argo CD for Kubernetes.
X


Cryptographically sign and attest container image provenance with Tekton chains.
X


Verify container image SLSA compliance against more than 40 rules.
X


Identify critical existing vulnerabilities with each merge request.
X



Who’s the target user? What user roles are available?

If you’re a platform engineer, you’re in the right place. Application developers and software security team members can make great use of {ProductShortName} too.

How does it all work?

Give us a few clicks, and we’ll get you started in just a few minutes. Input your repository URL and let {ProductShortName} get to work importing code, building a pipeline, generating a snapshot, testing your code, and ultimately deploying your application to the hybrid cloud. You quickly get your app out to the world and immediately see its value.

No, really. How does it work?

To better understand how {ProductShortName} works, take a look at the following descriptive list of the various components and technologies that support and are supported by {ProductShortName}. If you’re not into details, now’s a good time to put that scrolling finger to use.


Table 2. {ProductShortName} technologies and components






OpenShift
{ProductShortName} runs on the OpenShift CI/CD cloud-native platform. Its various services standardize workflows and make it easier to securely manage the entire development lifecycle.


GitLab
{ProductShortName} automatically starts a build according to the pipeline definition in your merge request (MR). You can also view MR test feedback according to the checks API, and after successful tests, you can set up your MRs to automerge.


Argo CD
Argo CD from GitOps declares and controls versions of your app definitions, configurations, and environments, and automates and tracks app deployment and lifecycle management.


Tekton build pipeline
When you build with {ProductShortName}, you store a complete Tekton build pipeline in your repository.


Tekton Chains
{ProductShortName} can use Tekton Chains to produce a signed build pipeline attestation.



Tell me more about security

We couldn’t be more serious about the T in {ProductShortName}. We support SLSA level 3 verification so you can more easily identify and address critical vulnerabilities. Whether it’s a source threat, dependency threat, or build threat, {ProductShortName} ensures your software supply chain’s authenticity and dependability.
