# Horizontal Pod Autoscaler

In Kubernetes, a HorizontalPodAutoscaler automatically updates a workload resource (such as a Deployment or StatefulSet), with the aim of automatically scaling the workload to match demand.

Horizontal scaling means that the response to increased load is to deploy more Pods. This is different from vertical scaling, which for Kubernetes would mean assigning more resources (for example: memory or CPU) to the Pods that are already running for the workload.

If the load decreases, and the number of Pods is above the configured minimum, the HorizontalPodAutoscaler instructs the workload resource (the Deployment, StatefulSet, or other similar resource) to scale back down.

```
minikube addons enable metrics-server
```

```
kubectl apply -f metrics_server.yaml
```

This will enable metrics server in the kube-system namespace. This is responsible for collecting the data from the pods and make it available to master node so that the control pannel will read the data and decide what to do based on the HPA/VPA defined.

Note: The metrics_server.yaml is the default yaml file that collects data about CPU and Memory usage. You can also define your own metrics server that monitors parametes mentioned by you.


## Create the Deployment, Service, Ingress and HPA


```
kubectl apply -f deployment.yaml
kubectl apply -f internal_service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f hpa.yaml
```

Explaining the above commands,
* Deployment will create 1 RS with 1 Pod.
* Internal service will create an Service of type ClusterIP.
* Ingress will give DNS support.
* HPA will be monitoring the pods and when times comes, it upscales the pod by changing the Deployment's RS Count

Things to check,
* Before running, make sure the Deployment, internal Service, Ingress, HPA are running.
* Give a request to the myapp.com/fibRec?n=20 and,
  * Check the CPU and memory Utilization.
  * Check the Replicas at HPA and replicaset info by watching **kubectl get all** command.
* Give a request to the myapp.com/fibRec?n=30 and,
  * Check the CPU and memory Utilization.
  * Check the Replicas at HPA and replicaset info by watching **kubectl get all** command.
* Give a request to the myapp.com/fibRec?n=30 and,
  * Check the CPU and memory Utilization.
  * Check the Replicas at HPA and replicaset info by watching **kubectl get all** command.
  * Here due to heavy increase in the CPU load by single Pod, HPA will schedule more pods in the cluster.
