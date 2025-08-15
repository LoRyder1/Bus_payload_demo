# on both VMs
sudo hostnamectl set-hostname cp1   # or w1 on the worker
echo "10.0.0.11 cp1
10.0.0.12 w1" | sudo tee -a /etc/hosts
