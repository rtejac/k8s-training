# Using locally build images on Minikube

Run the following command to use the locally build images in your deployment

```
minikube docker-env

FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env') DO @%i
```


# Build the image

```
docker build -t web_aaplication:v1.0 .
```

Replace the image name in the deployments to image name you gave here to use this image for Pods.
