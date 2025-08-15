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
	