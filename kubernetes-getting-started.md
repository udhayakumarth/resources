## Getting started
1️⃣ Install kubectl

2️⃣ Install Kubernetes cluster(ex: minikube)

3️⃣ Create namespace in cluster.

4️⃣ Create pod with docker image inside namespace

5️⃣ Expose the pod using service
  
* * *
### what is kubectl?
A CLI tool used to send commands to Kubernetes clusters.

### what is a cluster?
A Kubernetes cluster is a group of machines (nodes).  A cluster includes: Master and worker Node.

### what is a node?
A node is a machine inside a cluster that runs pods.

### what is a namespace?
A namespace in Kubernetes is a way to logically separate and organize resources within a cluster. 

### what is a pod?
A Pod is the smallest deployable unit in Kubernetes. It represents one or more containers that share the same network and storage.

### what is a service?
A Service in Kubernetes exposes a group of Pods to the network. Since Pods can be deleted, restarted, or moved to different nodes, a Service provides a consistent way to access them.

* * *
## How a node works?

![image](https://github.com/user-attachments/assets/b6d18108-5f5a-45c3-9ca4-7a94220e70b6)

### Main Component 
- Control Plane
- Worker Node

	#### Control Plane 
	- Api server
	- Controller manager
	- Scheduler
	- Etcd
	
	#### Worker Node
	- Kubelet
	- Container runtime
	- Kube-proxy
