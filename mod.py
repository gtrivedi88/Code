Yes, the gitop-repo could say "It invokes the gitops-pull-request pipeline (located in the pipelines directory)" so when you look at the description in the pipelines it says something like
Pipelines.  Implementations of build and promotion validation pipelines used referenced from the gitops-repo and source repo event handlers.

the source-repo  and gitops-repos contents get installed into users repositories, they can find what the pipelines are actually doing by looking into the pipelines directory
