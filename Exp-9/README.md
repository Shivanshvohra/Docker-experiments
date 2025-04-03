Minikube with Docker on Windows ☸️
🚀 Run Kubernetes Locally with Minikube & Docker 🐳

🌟 Introduction
Minikube is a lightweight Kubernetes tool that allows you to run a local cluster on your machine. It's perfect for developers looking to experiment with Kubernetes without setting up cloud infrastructure. Minikube works with various drivers like Docker, VirtualBox, and Hyper-V, making Kubernetes development easier than ever!

🛠️ Prerequisites
Before getting started, ensure you have the following installed:

✅ 1. Install Docker Desktop 🐋
Minikube runs Kubernetes inside a Docker container, so you need Docker Desktop:

Download Docker Desktop
Enable WSL 2 Backend (recommended) ⚙️
If on Windows Pro/Enterprise, enable Hyper-V 🔧
✅ 2. Install Minikube 📦
Run the following command in CMD or PowerShell (Admin):

choco install minikube
If you don't have Chocolatey, install Minikube manually.

✅ 3. Install kubectl (Kubernetes CLI) 🔗
choco install kubernetes-cli
Verify the installation:

kubectl version --client
🚀 Getting Started with Minikube & Docker
✅ Step 1: Start Minikube 🏁
Make sure Docker is running, then start Minikube using Docker as the driver:

minikube start --driver=docker
Check the status:

minikube status
🏗️ Deploying an Application
✅ Step 2: Deploy Nginx Web Server 🌐
1️⃣ Create an Nginx Deployment
kubectl create deployment nginx --image=nginx
2️⃣ Expose the Deployment
kubectl expose deployment nginx --type=NodePort --port=80
3️⃣ Get the Service URL
minikube service nginx --url
Open the provided URL in your browser to see Nginx running! 🎉

⚙️ Managing Kubernetes Cluster
✅ Check Running Pods 📋
kubectl get pods
✅ Scale the Deployment 📈
Increase replicas to 3:

kubectl scale deployment nginx --replicas=3
Check running pods:

kubectl get pods
✅ Delete Deployment 🗑️
kubectl delete service nginx
kubectl delete deployment nginx
❌ Stopping and Cleaning Up Minikube
✅ Stop Minikube 🔻
minikube stop
✅ Delete the Cluster 🗑️
minikube delete
This removes all Kubernetes resources.

🎯 Conclusion
By using Minikube with Docker, you can easily run Kubernetes locally without needing VirtualBox or Hyper-V. This setup allows developers to test and experiment with Kubernetes deployments effortlessly. 🚀🔥

💡 Next Steps:

Deploy custom applications in Minikube.
Explore Kubernetes resources like ConfigMaps, Secrets, and Volumes.
Learn how to use Helm charts for deploying applications.
💙 Happy Kubernetes-ing! ☸️🚢