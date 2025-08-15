# run simplest workload

kubectl create deployment hello --image=nginx --port=80
kubectl expose deployment hello --type=ClusterIP --port=80
kubectl port-forward svc/hello 8080:80
# browse http://localhost:8080


# validation check

kubectl get nodes

# both ready

kubectl get pods -A

#flannel DaemonSet running on both nodes

#Grafana reachable - dashboards populated
https://localhost:3000