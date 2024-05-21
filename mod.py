= Enabling a Snyk task

While a Snky test is available to run a build time in the default pipelines, additional configuration is needed to enable the test. This is an example of a build-time test that requires the configuration of a custom secret to be able to run.

The `sast-snyk-check` task uses the Snyk Code tool to perform static application security testing (SAST). 
Specifically, the Snyk check scans an application's source code for potential security vulnerabilities, 
including SQL injection, cross-site scripting (XSS), and code injection attack vulnerabilities.

NOTE: You can run a Snyk task only if you have a Snyk token stored in a namespace secret. 
You should also include the name of your secret in the *snyk-secret* pipeline parameter.
