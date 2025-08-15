helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install into a dedicated namespace
helm install kps prometheus-community/kube-prometheus-stack \
  -n monitoring --create-namespace

# Get into grafana

# port-forward Grafana to your laptop (keep this running)
kubectl -n monitoring port-forward svc/kps-grafana 3000:80

# get the auto-generated admin password (user is 'admin')
kubectl -n monitoring get secret kps-grafana \
  -o jsonpath='{.data.admin-password}' | base64 -d; echo
