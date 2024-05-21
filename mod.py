= Build-time tests

This document covers the build-time tests (formerly known as "sanity tests") that {ProductName} runs as part of its component build pipeline. These build-time tests automatically check all application images to ensure that they're up-to-date, correctly formatted, and protected from security vulnerabilities.

The {ProductName} component build pipeline supports several types build-time tests. The build-time tests used in {ProductName} are run in the form of https://tekton.dev/docs/pipelines/tasks/#overview[Tekton tasks]. The utility used for validating container information is https://www.conftest.dev/[Conftest]. The following tables show the currently implemented build-time tests:

.Deprecated image checks
|===
|Test name |Description |Failure message

|image_repository_deprecated |Deprecated images are no longer maintained, leading to unresolved security vulnerabilities. | The container image must not be built from a repository  marked as 'Deprecated' in COMET
|===

.Unsigned RPM check
|===
|Test name |Description |Failure message

|image_unsigned_rpms |Packages signed with Red Hat's secure signing server adheres to stringent policies and procedures. |All RPMs in the image must be signed. Found following unsigned rpms(nvra):
|===
