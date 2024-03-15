Running with gitlab-runner 16.4.2 (e77af703)
  on gitlab-runner2.cee.prod.upshift.rdu2.redhat.com 9d6aaa01, system ID: s_82e01d194e54
Resolving secrets
00:00
Preparing the "docker" executor
00:01
Using Docker executor with image registry.access.redhat.com/ubi9/ubi ...
WARNING: Container based cache volumes creation is disabled. Will not create volume for "/cache"
Pulling docker image registry.access.redhat.com/ubi9/ubi ...
Using docker image sha256:8d2a8803cfca17a81eb9412e1f33ae1c6fe3797553e9b819899dc03f1657cf12 for registry.access.redhat.com/ubi9/ubi with digest registry.access.redhat.com/ubi9/ubi@sha256:66233eebd72bb5baa25190d4f55e1dc3fff3a9b77186c1f91a0abdb274452072 ...
Preparing environment
00:00
Updating CA certificates...
WARNING: ca-cert-ca.pem does not contain exactly one certificate or CRL: skipping
Running on runner-9d6aaa01-project-83727-concurrent-0 via gitlab-runner2.cee.prod.upshift.rdu2.redhat.com...
Getting source from Git repository
00:01
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/software-supply-chain-documentation/rhtap/.git/
Created fresh repository.
Checking out 8562b2bd as detached HEAD (ref is main)...
Skipping Git submodules setup
Restoring cache
00:01
Checking cache for default-protected...
WARNING: file does not exist                       
Failed to extract cache
Checking cache for main...
WARNING: file does not exist                       
Failed to extract cache
Executing "step_script" stage of the job script
00:03
Using docker image sha256:8d2a8803cfca17a81eb9412e1f33ae1c6fe3797553e9b819899dc03f1657cf12 for registry.access.redhat.com/ubi9/ubi with digest registry.access.redhat.com/ubi9/ubi@sha256:66233eebd72bb5baa25190d4f55e1dc3fff3a9b77186c1f91a0abdb274452072 ...
$ dnf install -y asciidoctor rsync
Updating Subscription Management repositories.
Unable to read consumer identity
This system is not registered with an entitlement server. You can use subscription-manager to register.
Red Hat Universal Base Image 9 (RPMs) - BaseOS  2.0 MB/s | 515 kB     00:00    
Red Hat Universal Base Image 9 (RPMs) - AppStre 6.8 MB/s | 1.8 MB     00:00    
Red Hat Universal Base Image 9 (RPMs) - CodeRea 801 kB/s | 192 kB     00:00    
No match for argument: asciidoctor
Error: Unable to find a match: asciidoctor
Cleaning up project directory and file based variables
00:01
ERROR: Job failed: exit code 1
