Triggered by <a href="https://gitlab.cee.redhat.com/software-supply-chain-documentation/rhtap/merge_requests/40" target="_blank">GitLab Merge Request #40</a>: Gaurav Trivedi/feedback-update-customization => main
Loading library cp-jenkins@master
Attempting to resolve master from remote references...
 > git --version # timeout=10
 > git --version # 'git version 2.39.3'
 > git ls-remote -h -- https://gitlab.cee.redhat.com/cp-devops/cp-pipeline-libraries.git # timeout=10
Found match: refs/heads/master revision 97f7eef6d461696aa4aa025e7adfb2189920e9b6
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/CCS/ccs-mr-preview@libs/a3e22ea35bb7227bb9197b72809cb2257fc8244fa305c06e4ae238d7e0b595a9/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://gitlab.cee.redhat.com/cp-devops/cp-pipeline-libraries.git # timeout=10
Fetching without tags
Fetching upstream changes from https://gitlab.cee.redhat.com/cp-devops/cp-pipeline-libraries.git
 > git --version # timeout=10
 > git --version # 'git version 2.39.3'
 > git fetch --no-tags --force --progress -- https://gitlab.cee.redhat.com/cp-devops/cp-pipeline-libraries.git +refs/heads/*:refs/remotes/origin/* # timeout=10
skipping resolution of commit 38c8158afdcf99b8e4f4e7684f7b33ff70b08443, since it originates from another repository
Checking out Revision 97f7eef6d461696aa4aa025e7adfb2189920e9b6 (master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 97f7eef6d461696aa4aa025e7adfb2189920e9b6 # timeout=10
Commit message: "Updates CP to DXP in Notifications by email"
Loading library imperative-when@master
Attempting to resolve master from remote references...
 > git --version # timeout=10
 > git --version # 'git version 2.39.3'
 > git ls-remote -h -- https://github.com/comquent/imperative-when.git # timeout=10
Found match: refs/heads/master revision 9ee7fbb323f2b106c4404473cfca50a3948fe1a6
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/CCS/ccs-mr-preview@libs/83d623e09b01ca6bd44e3bf1f6648644361a5a5ff5d120343bd3f1872269af60/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/comquent/imperative-when.git # timeout=10
Fetching without tags
Fetching upstream changes from https://github.com/comquent/imperative-when.git
 > git --version # timeout=10
 > git --version # 'git version 2.39.3'
 > git fetch --no-tags --force --progress -- https://github.com/comquent/imperative-when.git +refs/heads/*:refs/remotes/origin/* # timeout=10
skipping resolution of commit 38c8158afdcf99b8e4f4e7684f7b33ff70b08443, since it originates from another repository
Checking out Revision 9ee7fbb323f2b106c4404473cfca50a3948fe1a6 (master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 9ee7fbb323f2b106c4404473cfca50a3948fe1a6 # timeout=10
Commit message: "Update LICENSE"
[Pipeline] Start of Pipeline
[Pipeline] timeout
Timeout set to expire in 30 min
[Pipeline] {
[Pipeline] node
Running on docker01 in /home/jenkins/workspace/CCS/ccs-mr-preview
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Build preview)
[Pipeline] dir
Running in /home/jenkins/workspace/CCS/ccs-mr-preview/doc-source
[Pipeline] {
[Pipeline] checkout
The recommended git tool is: NONE
using credential id-rsa-gitlab-cee
Fetching changes from the remote Git repository
Cleaning workspace
ERROR: Error fetching remote repo 'source'
hudson.plugins.git.GitException: Failed to fetch from git@gitlab.cee.redhat.com:software-supply-chain-documentation/rhtap.git
	at hudson.plugins.git.GitSCM.fetchFrom(GitSCM.java:999)
	at hudson.plugins.git.GitSCM.retrieveChanges(GitSCM.java:1241)
	at hudson.plugins.git.GitSCM.checkout(GitSCM.java:1305)
	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep.checkout(SCMStep.java:129)
	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:97)
	at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:84)
	at org.jenkinsci.plugins.workflow.steps.SynchronousNonBlockingStepExecution.lambda$start$0(SynchronousNonBlockingStepExecution.java:47)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:539)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
	at java.base/java.lang.Thread.run(Thread.java:840)
Caused by: hudson.plugins.git.GitException: Command "git reset --hard" returned status code 128:
stdout: 
stderr: error: unable to create symlink docs/modules/release-notes/cxf-parts/index.adoc: No such file or directory
error: unable to create symlink docs/modules/release-notes/cxf-parts/ref-camel-quarkus-cxf-rn.adoc: No such file or directory
fatal: Could not reset index file to revision 'HEAD'.

	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommandIn(CliGitAPIImpl.java:2842)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommandIn(CliGitAPIImpl.java:2762)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommandIn(CliGitAPIImpl.java:2757)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.launchCommand(CliGitAPIImpl.java:2051)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.reset(CliGitAPIImpl.java:705)
	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.clean(CliGitAPIImpl.java:1089)
	at jdk.internal.reflect.GeneratedMethodAccessor2600.invoke(Unknown Source)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at hudson.remoting.RemoteInvocationHandler$RPCRequest.perform(RemoteInvocationHandler.java:924)
	at hudson.remoting.RemoteInvocationHandler$RPCRequest.call(RemoteInvocationHandler.java:902)
	at hudson.remoting.RemoteInvocationHandler$RPCRequest.call(RemoteInvocationHandler.java:853)
	at hudson.remoting.UserRequest.perform(UserRequest.java:211)
	at hudson.remoting.UserRequest.perform(UserRequest.java:54)
	at hudson.remoting.Request$2.run(Request.java:377)
	at hudson.remoting.InterceptingExecutorService.lambda$wrap$0(InterceptingExecutorService.java:78)
	... 4 more
	Suppressed: hudson.remoting.Channel$CallSiteStackTrace: Remote call to docker01
		at hudson.remoting.Channel.attachCallSiteStackTrace(Channel.java:1787)
		at hudson.remoting.UserRequest$ExceptionResponse.retrieve(UserRequest.java:356)
		at hudson.remoting.Channel.call(Channel.java:1003)
		at hudson.remoting.RemoteInvocationHandler.invoke(RemoteInvocationHandler.java:285)
		at jdk.proxy105/jdk.proxy105.$Proxy200.clean(Unknown Source)
		at org.jenkinsci.plugins.gitclient.RemoteGitImpl.clean(RemoteGitImpl.java:532)
		at hudson.plugins.git.extensions.impl.CleanBeforeCheckout.decorateFetchCommand(CleanBeforeCheckout.java:46)
		at hudson.plugins.git.extensions.GitSCMExtension.decorateFetchCommand(GitSCMExtension.java:295)
		at hudson.plugins.git.GitSCM.fetchFrom(GitSCM.java:995)
		at hudson.plugins.git.GitSCM.retrieveChanges(GitSCM.java:1241)
		at hudson.plugins.git.GitSCM.checkout(GitSCM.java:1305)
		at org.jenkinsci.plugins.workflow.steps.scm.SCMStep.checkout(SCMStep.java:129)
		at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:97)
		at org.jenkinsci.plugins.workflow.steps.scm.SCMStep$StepExecutionImpl.run(SCMStep.java:84)
		at org.jenkinsci.plugins.workflow.steps.SynchronousNonBlockingStepExecution.lambda$start$0(SynchronousNonBlockingStepExecution.java:47)
		at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:539)
		... 4 more
[Pipeline] }
[Pipeline] // dir
[Pipeline] addGitLabMRComment
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] }
[Pipeline] // timeout
[Pipeline] End of Pipeline
ERROR: Error fetching remote repo 'source'
Finished: FAILURE
