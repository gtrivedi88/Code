kind create cluster
ERROR: failed to create cluster: failed to list nodes: command "docker ps -a --filter label=io.x-k8s.kind.cluster=kind --format '{{.Names}}'" failed with error: exit status 1
Command Output: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json?all=1&filters=%7B%22label%22%3A%7B%22io.x-k8s.kind.cluster%3Dkind%22%3Atrue%7D%7D": dial unix /var/run/docker.sock: connect: permission denied
