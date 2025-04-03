# Minikube with Docker on Windows ☸️


🚀 **Run Kubernetes Locally with Minikube & Docker** 🐳

---

## 🌟 Introduction

**Minikube** is a lightweight Kubernetes tool that allows you to run a local cluster on your machine. It's perfect for developers looking to experiment with Kubernetes without setting up cloud infrastructure. Minikube works with various drivers like Docker, VirtualBox, and Hyper-V, making Kubernetes development easier than ever!

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed:

### ✅ 1. Install Docker Desktop 🐋

Minikube runs Kubernetes inside a Docker container, so you need Docker Desktop:
- [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
- Enable **WSL 2 Backend** (recommended) ⚙️
- If on Windows Pro/Enterprise, enable **Hyper-V** 🔧

### ✅ 2. Install Minikube 📦

Run the following command in **CMD or PowerShell (Admin):**
```bash
choco install minikube
```
_If you don't have Chocolatey, [install Minikube manually](https://minikube.sigs.k8s.io/docs/start/)._

### ✅ 3. Install kubectl (Kubernetes CLI) 🔗

```bash
choco install kubernetes-cli
```
Verify the installation:
```bash
kubectl version --client
```

---

## 🚀 Getting Started with Minikube & Docker

### ✅ Step 1: Start Minikube 🏁

Make sure Docker is running, then start Minikube using Docker as the driver:
```bash
minikube start --driver=docker
```
Check the status:
```bash
minikube status
```

---

## 🏗️ Deploying an Application

### ✅ Step 2: Deploy Nginx Web Server 🌐

#### 1️⃣ Create an Nginx Deployment
```bash
kubectl create deployment nginx --image=nginx
```

#### 2️⃣ Expose the Deployment
```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

#### 3️⃣ Get the Service URL
```bash
minikube service nginx --url
```
Open the provided URL in your browser to see Nginx running! 🎉

---

## ⚙️ Managing Kubernetes Cluster

### ✅ Check Running Pods 📋
```bash
kubectl get pods
```

### ✅ Scale the Deployment 📈
Increase replicas to 3:
```bash
kubectl scale deployment nginx --replicas=3
```
Check running pods:
```bash
kubectl get pods
```

### ✅ Delete Deployment 🗑️
```bash
kubectl delete service nginx
kubectl delete deployment nginx
```

---

## ❌ Stopping and Cleaning Up Minikube

### ✅ Stop Minikube 🔻
```bash
minikube stop
```

### ✅ Delete the Cluster 🗑️
```bash
minikube delete
```
_This removes all Kubernetes resources._

---

## 🎯 Conclusion

By using **Minikube with Docker**, you can easily run Kubernetes locally without needing VirtualBox or Hyper-V. This setup allows developers to test and experiment with Kubernetes deployments effortlessly. 🚀🔥

💡 **Next Steps:**
- Deploy custom applications in Minikube.
- Explore Kubernetes resources like ConfigMaps, Secrets, and Volumes.
- Learn how to use Helm charts for deploying applications.

💙 **Happy Kubernetes-ing!** ☸️🚢
