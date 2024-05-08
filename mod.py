Konflux
Overview
Konflux is a platform for building integrated software that streamlines, consolidates, and secures the development lifecycle.

Goals
Compose software that consists of multiple components, from multiple repositories.
Provide transparency on the software supply chain, including both what makes up the software and how it was built.
Provide a way for software teams to release to destinations under the control of their SRE or release engineering team(s).
Rapid bootstrapping of new software projects
Support both existing and new projects
Provide APIs to manage your software lifecycle
Provide a surface for partners to integrate, add value
Provide a unified user interface across the entire process
Architecture Goals
Build artifacts once with enough data to determine suitability for releasing.
Build artifacts once that can be released to multiple locations, multiple use cases.
Specify builds and their dependencies entirely from git and not from transient state of the build system. Employ tools like renovate to manage dependency updates.
Build semantic reproducible artifacts. Any configuration which has the potential to affect the semantic functionality of a build should be source controlled and associated with the produced artifact (via the provenance, for example).
Be extensible. Provide opinionated build pipelines and release pipelines, but let users extend those and create their own.
"Shift left" the decisions for releasing into PRs; you should be able to release artifacts from a PR as soon as it is merged.
Just in time scaling: In contrast to “just in case” scaling. The system should be able to scale without capacity reserved ahead of time.
Static stability: the overall system continues to work when a dependency is impaired.
Enhancements to the pipelines (the extensible elements of the system) should be rolled out in such a way that individual users can control when they accept the update to their workspaces, their processes. Use policy to drive eventual compliance.
Each subservice can fulfill its primary use cases independently, without relying on other systems’ availability. An exception to this is the tekton [pipeline service] which provides foundational APIs on which build-service, integration-service, and release-service depend.
Each sub-service owns its data and logic.
Communication among services and participants is always asynchronous.
Each sub-service is owned by one team. Ownership does not mean that only one team can change the code, but the owning team has the final decision.
Minimize shared resources among sub-services.
Participants: onboarding new participants, the flexibility to satisfy the technology preferences of a heterogeneous set of participants. Think of this as the ability to easily create an ecosystem and the ability to support that ecosystem’s heterogeneous needs.
Security, Privacy, and Governance: Sensitive data is protected by fine-grained access control
