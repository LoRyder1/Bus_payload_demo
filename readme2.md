## Data pipeline
	- Bus telemetry Producer Pod
		- http /metrics
	- Kubernetes Service
		- stable name/DNS
	- Prometheus
		- Operator stack
			- service discovery via ServiceMonitor
			- scrapes metrics on a schedule pull
			- stores amples in local TSDB
			- evaluates alert rules - alertmanager
	- Grafana
		- queries prometheus for panels
		- dashboards, annotations, ad hoc views
		- dashboard alerts

## What is happening

1. Producer emits metrics
	- bus pod exposes live housekeeping values
2. Kubernetes gives it an address
	- A Service gives the pod a stable DNS name
	- pods can come and go; the Service stays put
3. Prometheus discovers and scrapes
	- A ServiceMonitor tells Prometheus which SErvice to srape, which port/path and how often
	- Prometheus pulls /metrics over HTTP, attaches Kubernetes labels, and stores samples in its TSDB
4. Rules run; alerts fire if needed
5. Grafana visualization

## Each component's role

### Kubernetes
	- orchestration and self-healing
	- service discovery
	- scaling and placement
	- security and boundaries
	- repeatability

### Prometheus
	- pull-based collection
	- labeling and queries
	- local tsdm
	- alerting engine

### Grafana
	- Dashboards
	- Exploration
	- Team visibility
	
## what you have

1. Cluster - 1 control plane, 1 worker
	- containerd, kubeadm, init/join, CNI, CoreDNS healthy
2. Observability
	- kube-prometheus-stack - prometheus, alertmanager, Grafana, node-exporter, kube-state-metrics
3. Workload
	- a tiny bus-telemetry exporter HTTP /metrics + Service + ServiceMonitor + alert rules
	

## Overview of Kubernetes
1. Control Plane
	- API Server
	- Scheduler
	- Controller Manager
	- etcd
2. Worker Node
	- Kubelet
	- Kube-proxy
	- Container Runtime

## Key Kubernetes Objects
1. Pod
2. Deployment
3. Service
4. ConfigMap & Secret
5. Ingress
6. Namespace

## Networking in Kubernetes
1. Pod to Pod communication
2. Service to Pod routing
3. Ingress

## Cluster Lifecycle
1. Provisioning
2. Deploying Applications
3. Scaling
4. Upgrading and Maintenance

