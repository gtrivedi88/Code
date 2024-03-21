|image_repository_deprecated |N/A |Deprecated images are no longer maintained and will accumulate security issues without releasing a fixed version | The container image should not be built from a repository which is marked as 'Deprecated' in COMET
|image_repository_deprecated |Deprecated images are no longer maintained and will accumulate security issues without releasing a fixed version | The container image should not be built from a repository which is marked as 'Deprecated' in COMET
|===

.Unsigned RPM check
|===
|Test name |Label name |Description |Failure message
|Test name |Description |Failure message

|image_unsigned_rpms |N/A |Providing packages signed with the secure Red Hat signing server indicates that the package was subject to all appropriate policies and procedures |All RPMs found on the image must be signed. Found following unsigned rpms(nvra):
|image_unsigned_rpms |Providing packages signed with the secure Red Hat signing server indicates that the package was subject to all appropriate policies and procedures |All RPMs found on the image must be signed. Found following unsigned rpms(nvra):
|===
