# Simplest possible setup for Bus and payload

## k8s - 1 physical server, 1 control plane, 1 worker node

## kubernetes configuration and installation for using grafana and k8s to run a workload

# Setting up k8s - a small town

	- setting up a small town with two buildings, a control center and workshop
	- also setting a monitoring station - Grafana
## Prepared the land
	- disabled swap, turn on IPv4 forwarding and loaded networking modules

## chose delivery trucks
	- installed containerd - container runtime - so Kubernetes can run containers

## set up the town council
	- installed kubeadm, kubelet, and kubectl on both the control center and workshop

## built control center
	- ran kubeadm init on control plane VM

## build the roads
	- installed Flannel CI so pods can talk to each other across nodes

## invited workshop
	- kubeadm join

## built monitoring tower
	- kube-prometheus-stack

- opened first shop
	- created an NGINX Deployment and Service
- prove whole town works
	- both buildings - control and workshop are active and connected
	- roads - flannel network
	- watchtower - Grafana
	
- town can no handle more buildings - apps, more roads - services, more watchtowers