# Helm Charts


## Installing Helm on Windows

  * Goto helm github [repo](https://github.com/helm/helm/releases)
  * Select the Windows amd64 binary.
  * Download the executable.


### Add Helm location to PATH environmental variable.
  * Open System Properties. Click on Advanced tab.
  * Select Environmental Variables on bottom right side.
  * Go to System variabels and check for Path variable.
  * Click on that and click on Edit option.
  * Then in the Edit Environmental variable window, click on the New button paste the helm installable location and then click on Ok until you reach till System properties window.
  * And then Click on Ok and the window will be automatically closed.
  * Run the executable to install helm

Helm is the package manager for Kubernetes. Like apt for Ubuntu, pip for Python, helm is for Kubernetes.

## Basic commands in helm

### Create a default template
```
helm create mychart
```
This will create a directory named mychart

### Check the files and values before running the chart
```
helm install --dry-run chartName mychart
```
This will print all files in templates directory with values replaced by values.yaml file

### Run the chart
```
helm install chartName mychart
```
This will run the yaml flies in the templates directory with values replaced by values.yaml file

### List down the helm charts availabe
```
helm ls
```

### Provide values other than values.yaml to override the default values
```
helm install -f mychart/override_values.yaml chartName mychart
```

This will only override the values given in override_values.yaml file, rest all will be taken from values.yaml

### Upgrade the helm with new values or files
```
helm upgrade chartName mychart
```

This will upgrade the helm revision


### Rollback to previous revisions
```
helm rollback chartName revisionNumber
```


### Package the chart
```
helm package chartName
```

This will create a **tgz** file with name as chartName(from Chart.yaml)_chartVersion(from Chart.yaml).tgz

### Uninstall helm
```
helm uninstall chartName
```

This will delete the components created by running the yaml flies in the templates directory with values replaced by values.yaml file
