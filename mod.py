Setting up OpenShift Pipelines to deploy application to pre production environment and view Enterprise contract policies reports 
To deploy your latest code change to pre-prod environment, you create Pipea tag in Github or GitLab which triggers a deploy-focuseed Tekton pipeline, which updates the GitOps repository causing ArgoCD to deploy. When you create a tag, it automatically triggers a Pipeline Run which you can review in the CI tab. This Pipeline Run has a task called verify-enterprise-contract that compares your application against a set of enterprise contract policies to verify if it meets them before moving your application to pre-products. It displays the scan resultsin the  View output icon in the CI tab > Actions column is designed to provide insights into security vulnerabilities identified during the scans.
An application’s build process uses Tekton Chains to produce a signed in-toto attestation of the build pipeline. The Enterprise Contract then uses this attestation to verify the build’s integrity and compliance with a set of policies. These policies include best practices and any organization-specific requirements.


The main goal of the enterprise contract (EC) is to prevent the release of artifacts that are not compliant with the Supply chain Levels for Software Artifacts (SLSA) security framework. Organizations can implement their policies by expressing them as criteria for valid artifacts within the EC. Developers then access the EC as an object inside the workspace. As a developer, reference the EC to verify what must be true about your build and how to make your artifacts compliant with your organization’s needs and policies. The EC evaluates the policy definitions against the collected provenance data, ensuring that the build process complies with the enterprise policy. Some examples of the EC policy rules include the following use cases:
Verify the execution of a set of Tekton Tasks. For example, the EC can assert that a certain Tekton Task, which performs anti-virus checks, ran successfully.
Verify that all used Tekton Tasks match an expected version and origin.
Verify that an expected signature key properly signed built artifacts.


.Procedures
In the Developer or Administrator perspective, switch to the relevant project where you want a visual representation of SBOMs.
Update your existing scan task with annotations in the following format:


apiVersion: tekton.dev/v1
kind: Task
metadata:
 name: enterprise-contract-task <1>
 annotations:
    task.results.format: application/json <2>
    task.results.type: ec <3>
    task.output.location: logs
    task.results.container: step-report-json <4>
spec: …
      steps:
        - name: report-json
          image: quay.io/enterprise-contract/ec-cli:snapshot@sha256:33be4031a3316a46db3559a4d8566bc22f9d4d491d262d699614f32f35b45b67 <5>
          command: [cat]
          args:
            - "$(params.HOMEDIR)/report-json.json"
<1> Task name. For example, enterprise-contract-task
<2> The supported result format
<3> Type of scan tool. For example, ec.
<4> The name of the container to get the POD logs.
<5> The URL of the image to scan.


.Verification
Go to Catlog and select the component that you want to move to pre-production environment.
On the Overview tab, select View Source. The system, in a new tab, displays your source repository which can either be in GitHub or GitLab. 
If your repository is on GitLab, go to Reposiroty > Tags and select Create tag.
In the Tag name field, enter v.1 and select Create tag.
Alternatively, if your repository is on GitHub, go to
On the CI tab, review the pipeline run.

Select the View output icon in the Actions column. The system displays a pop-up window.
