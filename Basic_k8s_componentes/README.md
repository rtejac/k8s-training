# Basic Kubernetes components

We can create any Kubernetes component with either imperative (complete CLI) or declarative (Using YAML files) syntax. YAML files will give more control and will be easy to use.

## Pod

The smallest unit in the Kubernetes world.

```
kubectl apply pod.yaml
```
This will create a pod with the container images mentioned in the specs.container.image of yaml flie.

Run this command to view running pods
```
kubectl get pods
```
Delete the pod
```
kubectl delete -f pod.yaml
```
or
```
kubectl delete pod <pod name>
```

### Replicaset
An abstraction on top of the pods that can recreate a pod if it crashes/destroys
```
kubectl apply -f replicaset.yaml
```
To see replicasets available, run
```
kubectl get rs
```
Delete a pod and see what happens, then delete the replicaset and see what happens.

### Deplpoyment
An abstraction on top of the replicaset that can recreate a pod or replicaset if it crashes/destroys
```
kubectl apply -f deployment_0.yaml
```

Check what are all running when you create a deployment.
```
kubectl get all
```
Deployment will create a replicaset for us and replicaset will create pods under it.

Now if the pods crash, replicaset will create new ones, and if the replicaset crashes, deployment will take care of creating new replicaset and that new replicaset will create pods under it.

Try deleting pod, replicaset individually once

### Service
Each pod that is created will have its own IP and that IP will be dynamic. i.e, if the pod dies and a new pod is replaced, then the IP of the new pod will be different.

So we need a static IP which we can relay on to communicate to pods. That's where the Service comes in.

Service will give a static IP to us and binds to all pods that are matching the selecting criteria. That way when we request to a Service, the request will land on any of the pod that is connected to the Service

Enough theory was given in the training session, run the following to create an internal or external service.
```
kubectl apply -f external_servcie_0.yaml
                (or)
kubectl apply -f internal_servcie_0.yaml
```

### Ingress
Ingress will provide a DNS to the service and make the service accessible only within cluster(if the service type is ClusterIP).

In order for the ingress to work, we need an ingress controller which will evaluate the rules and direct the traffic to specified services. There are many ingress controllers available, but most commonly used controller is from **NGINX**

To install ingress controller, run

```
minikube addons enable ingress
```

To verify the ingress controller, run the following command, you will see some pods and deployments running
```
kubectl get all -n ingress-nginx
```

```
kubectl apply -f ingress_0.yaml
```
Verify the ingress running
```
kubectl get ingress
```


After this, edit the **C:\Windows\System32\drivers\etc\hosts** file with **node_ip domain_name_you_gave_in_the_ingress_file**

```
minikube node ip #This will give node ip
```

Then go to browser and type(only for this example, change the url based on the name you gave in the ingress file)
```
http://myapp.com/
```


### StatefulSet
Statefulsets will give control ove pods order of deployments and will be used if an application is Stateful.

Stateless application which won't depend on previous state will be deployed using Deployments.


```
kubecl apply -f statefulset.yaml
```
After running this, verify the following,
* Names of the pods created.
* Order of pods creation.
* What happens when the number of replicas are
  * Increased.
  * Decreased.
* In which order the pods are getting destroyed when the statefulset is deleted or replicas are decreased.