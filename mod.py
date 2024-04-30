(Optional) If you do not have a vulnerability scan task, create one in the following format:
+
*Example vulnerability scan task using Roxctl*
+
[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Task
metadata:
  name: vulnerability-scan  # <1>
  annotations:
    task.output.location: results  # <2>
    task.results.format: application/json
    task.results.key: SCAN_OUTPUT  # <3>
spec:
  results:
    - description: CVE result format  # <4>
      name: SCAN_OUTPUT
      value: string
  steps:
    - name: roxctl  # <5>
      image: quay.io/roxctl-tool-image  # <6>
      env:
        - name: ENV_VAR_NAME_1  # <7>
          valueFrom:
            secretKeyRef:
              key: secret_key_1            
              name: secret_name_1
      env:
        - name: ENV_VAR_NAME_2
          valueFrom:
            secretKeyRef:
              key: secret_key_2            
              name: secret_name_2
      script: | # <8>
        #!/bin/sh
        # Sample shell script
        echo "ENV_VAR_NAME_1: " $ENV_VAR_NAME_1
        echo "ENV_VAR_NAME_2: " $ENV_VAR_NAME_2
        jq --version (adjust the jq command for different JSON structures)
        curl -k -L -H "Authorization: Bearer $ENV_VAR_NAME_1" https://$ENV_VAR_NAME_2/api/cli/download/roxctl-linux --output ./roxctl
        chmod +x ./roxctl 
        echo "roxctl version"
        ./roxctl version
        echo "image from pipeline: " 
        
        # Replace the following line with your dynamic image logic
        DYNAMIC_IMAGE=$(get_dynamic_image_logic_here)
        echo "Dynamic image: $DYNAMIC_IMAGE"
        ./roxctl image scan --insecure-skip-tls-verify -e $ENV_VAR_NAME_2 --image $DYNAMIC_IMAGE --output json  > roxctl_output.json
        more roxctl_output.json
        jq -rce \  # <9>
          '{vulnerabilities:{
          critical: (.result.summary.CRITICAL),
          high: (.result.summary.IMPORTANT),
          medium: (.result.summary.MODERATE),
          low: (.result.summary.LOW)
            }}' scan_output.json | tee $(results.SCAN_OUTPUT.path)
----
<1> The name of your task.
<2> The location for storing the task outputs.
<3> The naming convention of the scan task result. A valid naming convention must end with the `SCAN_OUTPUT` string. For example, SCAN_OUTPUT, MY_CUSTOM_SCAN_OUTPUT, or ACS_SCAN_OUTPUT.
<4> The description of the result.
<5> The name of the vulnerability scanning tool that you have used. 
<6> The location of the actual image containing the scan tool.
<7> The tool-specific environment variables.
<8> The shell script to be executed with json output. For example, scan_output.json.
<9> The format to extract vulnerability summary (adjust `jq` command for different JSON structures).
+
[NOTE]
====
This is just an example. Do not copy paste this as is. Update the values as per your scanning tool to set the results in the expected format.
====
