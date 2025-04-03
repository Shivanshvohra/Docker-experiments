🚀 Docker Network Experiment
This repository demonstrates how to create and test a custom Docker network (net-bridge) with multiple containers for seamless inter-container communication. The experiment showcases how containers can communicate within a user-defined bridge network.

🛠 Experiment Overview
Docker provides powerful networking capabilities, allowing containers to communicate securely. This experiment involves:

Creating a custom bridge network for isolated communication.
Running multiple containers within the network.
Inspecting and verifying connectivity between containers.
Testing inter-container communication using ping and name resolution.
🔧 Experiment Setup
1️⃣ Create a Custom Docker Network
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 net-bridge
2️⃣ Run Containers and Attach to the Network
🗄 Run Database Container
docker run -itd --net=net-bridge --name=cont_database redis
🖥 Run Server Container
docker run -dit --name server-A --network net-bridge busybox
3️⃣ Inspect Network and Containers
🔍 Check Network Details
docker network inspect net-bridge
🔎 Check Container Details
docker inspect cont_database
🌐 Get Container IP Address
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cont_database
4️⃣ Testing Connectivity
🖥 Access Container Shell
docker exec -it server-A sh
🔗 Ping Another Container by IP
ping 172.20.240.X  # Replace with actual container IP
🔗 Ping Another Container by Name
ping cont_database
📌 Observations
✅ The custom bridge network allows direct communication between containers.

✅ Containers can communicate using assigned IP addresses.

✅ Name resolution may not always work with BusyBox due to its minimal nature.

✅ Using docker inspect helps retrieve network details and assigned IPs.

🏁 Conclusion
This experiment highlights Docker's networking capabilities, demonstrating inter-container communication via a custom bridge network. Understanding Docker networking is crucial for deploying microservices and containerized applications efficiently.