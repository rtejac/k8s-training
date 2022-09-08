# Volumes

Volumes are used to store the data so that if a pod has to restart, all the data created by previous pod would still be available.

## Basic commands for Volumes


### Create a Deployment with Local volume(hostPath)
```
kubectl apply -f local_vol_hostpath.yaml
```
This will create a Deployment where the pods will be using the local volume from the node.

### Create a StorageClass
```
kubectl apply -f local_sc.yaml
```
This will create a Storage class.

### Create a PersistantVolumeClaim
```
kubectl apply -f local_volume_pvc.yaml
```
This will create a PVC.

Then check the following outputs,

```
kubectl get sc #Lists down all the available SCs
kubectl get pvc #Lists down all the available PVCs
kubectl get pv #Lists down all the available PVs
```

### Create a Deployment using PVC
```
kubectl apply -f local_vol_dep.yaml
```
This will create a Deployment that uses the volumes claimed by PVC after a request made to SC which created PV automatically.


# ConfigMaps and Secrets as Volumes

By now we know that we can use ConfigMaps and Secrests to share the data to pods in a key value pair format. But other than that, we can also share the files using ConfigMaps and Secrets.

### Create a ConfigMap and Secret
```
kubectl apply -f cm_and_sec.yaml
```
This will create a ConfigMap and Secret resource that can be used to mount the path and use in the pods


### Create a Deployment which using the ConfigMap and Secret
```
kubectl apply -f cm_s_vol_mounted_dep.yaml
```
This will create a Deployment that uses the ConfigMap and Secret resource
