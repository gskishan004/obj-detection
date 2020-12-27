## Objective :
* Build a single application for object detection in contrasting datasets (coco and bloodcell).
* Analyze/compare relative performance of models on cloud platforms and Baremetal based on
the execution time as well as the model’s loss function thereby accounting for both the cloud
and machine learning aspects.
* [Furthermore, for demo - create a docker image for the entire application hosted on
IBM cloud using Kubernetes for orchestration.](http://159.122.181.44:32073/) 

## Repo Contains:

* Code - contains code and dataset 
* logs - containes logs for cloud and baremetal
* baremetal run.txt - contains all the commands used for baremetal
* Dockerfile - contains docker file for dockerization
* deploy.yaml & service.yaml - YAML files for Kubernetes
* training_driver.ipynb - notebook for running code on cloud

For more details about the results and steps, refer to **Report and Steps.pdf**