== Customizing the sample pipeline template repository to your workflow

The sample pipeline template repository serves as a starting point. You can further customize it based on your organization's specific needs:

On the pipeline templates repository you will find following template pipelines:

* `docker-build-rhtap`: This pipeline is used to create dockerfile based sscs builds. The pipeline run by this runner will clone the source, build an image with SBOM, and attestations and push these to the users image registry.

* gitops-repo: This pipeline is used to validate pull-requests into the gitops repository. This runner will call the gitops-pull-request pipeline which will validate the images being updated. Its' designed to be used for promotion flows, where the state of one environment is being promoted to the successor environment (dev to stage, or stage to prod).

* pipelines:    

* This pipeline is used to create dockerfile based sscs builds. The pipeline run by this runner will clone the source, build an image with SBOM, and attestations and push these to the users image registry.

* tasks: add new tasks or modify existing ones to suit your requirements. For example, you can replace ACS tasks with some other checks or add new tasks into the pipeline.
