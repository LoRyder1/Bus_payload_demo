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


# Setup for Satellite bus telemetry

## K8s town is up
	- control plane, worker, Grafana/Prometheus

## minimal end to end satellite bus housekeeping setup
	- a little telemetry shed with few gauges on the wall
		- voltage, temp, battery SOC
	- Prometheus is the insepctor 
	- Grafana is the scoreboard

## what you'll deploy
	- namespace - sat-bus - where telemetry pod lives
	- telemetry producer - tiny python app that exposes Prometheus metrics on /metrics
	- service - stable address for Prometheus to scrape
	- ServiceMonitor - tells Prometheus Operator what to scrape
	- PrometheusRule - simple alerts - low voltage, high temp, no telemetry

### after bus-telemetry is applied
	- verify it's alive
		- kubectl -n sat-bus get pods,svc
		- kubectl -n sat-bus port-forward svc/bus-telemetry 8000:8000
		- curl -s http://localhost:8000/metrics | grep -E 'bus_supply|battery|imu_temp|bus_mode|heartbeat'

bash:

\```bash
# Prometheus UI (optional)
kubectl -n monitoring port-forward svc/kps-prometheus 9090:9090
# -> open http://localhost:9090 and query: bus_supply_voltage_volts

# Grafana (from your previous setup)
kubectl -n monitoring port-forward svc/kps-grafana 3000:80
# -> open http://localhost:3000, create a new dashboard with these queries:
#   - Stat: bus_supply_voltage_volts
#   - Gauge: bus_battery_soc_percent
#   - Time series: bus_imu_temp_celsius
#   - Stat: histogram_quantile(0.5, sum(rate(prometheus_http_request_duration_seconds_bucket[5m])) by (le))  (just to see queries work)
\```
