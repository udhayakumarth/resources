To start minikube:

`minikube start --driver=docker`

`minikube start --driver=virtualbox`

`minikube start --driver=none`

To connect with minikube:
`minikube ssh`

To check minikube all cluster status
`minikube profile list`

To Create a Second Cluster
`minikube start -p my-second-cluster --driver=virtualbox`

To Switch Between Clusters
`minikube profile my-second-cluster`

To stop a cluster
`minikube stop -p my-second-cluster`

To delete a cluster
`minikube delete -p my-second-cluster`



