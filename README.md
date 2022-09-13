# K8s-training

## Download required packages

### Minikube
Minikube is a single node Kubernetes Cluster which we can use to practice our Kubernetes examples


Install [Minikube for windows](https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe). Run the executable and follow the steps to complete its installation.

### Add Minikube location to PATH environmental variable.

* Open System Properties. Click on Advanced tab.
* Select Environmental Variables on bottom right side.
* Go to System variabels and check for Path variable.
* Click on that and click on Edit option.
* Then in the Edit Environmental variable window, click on the New button paste the minikube location and then click on Ok until you reach till System properties window.
* And then Click on Ok and the window will be automatically closed.



### Minikube need a Virtual environment to run.
Install [Oracle Virtual box on Windows](https://download.virtualbox.org/virtualbox/6.1.38/VirtualBox-6.1.38-153438-Win.exe). Run the executable and follow the steps to complete its installation.

### Kubectl

Click here to download [kubectl for windows](https://dl.k8s.io/release/v1.25.0/bin/windows/amd64/kubectl.exe). Run the executable and follow the steps to complete its installation.


## After installing all 3 packages

### Run the following
Start Minikube and check the version. This is expected to take some 4-5 mins based on your internet connection
```
minikube start
minikube version
```


By default, minikube will start single node Cluster. If you want to start a multinode Cluster, run

```
minikube start --nodes <desired_number_of_nodes> -p multinode
```


Check the pods, deployments running in the cluster. You will see a **service/kubernetes** , don't worry it's a default  one created.
```
kubectl get all
```

## Now for each demo/folder present in this repo, there is a readme file present. Use that to follow along.
