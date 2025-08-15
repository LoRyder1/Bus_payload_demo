# on VM1 (cp1)
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# as your regular user on cp1
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# on VM1
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml

# Join the worker
kubeadm token create --print-join-command

# verify

# back on VM1
kubectl get nodes -o wide

# install Helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
helm version
