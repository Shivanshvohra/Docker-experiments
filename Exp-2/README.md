# Docker Experiment 2: Binary Classification WebApp with Streamlit

Welcome to **Docker Experiment 2**! This project demonstrates the power of **Docker** to containerize a **machine learning web application** built using **Streamlit**. The app classifies mushrooms as either **edible** or **poisonous** based on input features, utilizing machine learning classifiers.

---

## 🚀 Project Overview

This is a **Binary Classification WebApp** designed to predict whether a mushroom is edible or poisonous using machine learning models. The app offers a selection of classifiers, such as **Support Vector Machine (SVM)**, **Logistic Regression**, and **Random Forest**.

### Key Features:
- **Interactive UI** built with **Streamlit** for classification and visualization.
- **Multiple Classifiers**: Choose between **SVM**, **Logistic Regression**, and **Random Forest**.
- **Evaluation Metrics**: View **Confusion Matrix**, **ROC Curve**, and **Precision-Recall Curve**.
- **Dockerized App**: Easy deployment and isolated environment.

---

## 📝 Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**: [Download and install Docker](https://www.docker.com/get-started)
- **Docker Compose**: For managing multi-container Docker applications.

---

## 📂 Project Structure

```plaintext
/Docker_Practices
├── /Exp-2
    ├── Dockerfile                 # Dockerfile to build the container image
    ├── docker-compose.yml         # Docker Compose configuration file
    ├── app.py                     # Streamlit app for mushroom classification
    ├── requirements.txt           # Python dependencies
    └── mushrooms.csv              # Mushroom dataset for classification
```

---

## 🚀 How to Run the Project

Follow the steps below to get the app up and running in your local environment.

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Shivanshvohra/Docker-experiments
cd Docker-experiments/Exp-2
```

### Step 2: Build the Docker Image

To build the Docker image, run the following command:

```bash
docker-compose build
```

This command will read the Dockerfile and build the image for the container.

### Step 3: Run the Docker Container

Once the image is built, start the container using:

```bash
docker-compose up
```

Now, the app will be available at http://localhost:8501.

### Step 4: Interact with the App

Open your browser and go to http://localhost:8501.
- Select a classifier (SVM, Logistic Regression, or Random Forest) from the sidebar.
- Adjust the hyperparameters and metrics to visualize (Confusion Matrix, ROC Curve, Precision-Recall Curve).
- Click Classify to see the results and metrics.

### Step 5: Stop the Application

To stop the application and the Docker container:

```bash
docker-compose down
```

---

## 🧑‍💻 Additional Docker Commands

Here are some additional commands to help you manage and check the status of your Docker containers:

### Check Running Containers

To check if your container is running, use:

```bash
docker ps
```

This will list all running containers along with their status and exposed ports.

### View Logs

To view the logs of your running container (helpful for debugging), use:

```bash
docker-compose logs
```

This will show you the logs from all containers in the Compose setup. To check logs for a specific container, use:

```bash
docker-compose logs <service_name>
```

For example:

```bash
docker-compose logs dockerex2
```

### Running Docker Compose in Detached Mode

To run the containers in the background (detached mode), use the following command:

```bash
docker-compose up -d
```

This will start your container in the background, allowing you to use the terminal for other tasks.

### Stopping Containers

To stop all running containers:

```bash
docker-compose down
```

Alternatively, you can stop just the app container:

```bash
docker-compose stop dockerex2
```

### Rebuild and Restart Containers

If you make changes to the Dockerfile or any other configurations, rebuild and restart the containers using:

```bash
docker-compose up --build
```

This command will rebuild the images and restart the containers with the updated configurations.

### Remove Unused Containers and Images

To remove any stopped containers and unused images, run:

```bash
docker system prune
```

Be careful with this command as it will remove all unused data. You can also remove just unused images with:

```bash
docker image prune
```

---

## 🛠 Dockerfile Breakdown

The Dockerfile is used to create a lightweight and efficient image for this web application. Here's a summary of what it does:

- **Base Image**: Uses python:3-slim for a minimal Python environment.
- **Install Dependencies**: Installs necessary libraries from requirements.txt.
- **Working Directory**: Sets /app as the working directory inside the container.
- **Non-root User**: Runs the app as a non-root user for added security.
- **Port Exposure**: Exposes port 8501 for Streamlit.
- **Run Command**: Uses `streamlit run app.py` to start the app.

---

## 🧑‍💻 Dependencies

This app relies on the following Python libraries:

- **pandas**: For data manipulation.
- **streamlit**: For building the web interface.
- **scikit-learn**: For machine learning models and evaluation metrics.
- **matplotlib**: For plotting visualizations.

---

## 🤝 Contributing

Feel free to fork the repository and submit a pull request with your improvements! If you encounter any issues or have feature requests, please open an issue on GitHub.

---

### Happy Coding! 🎉

___

## Streamlit Python Code for Mushroom Classification

```python
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('mushrooms.csv')

data = load_data()

# Show dataset in the app
st.write("Mushroom Dataset", data.head())

# Features and target column
X = data.drop(columns=["class"])
y = data["class"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sidebar: Classifier selection
classifier_option = st.sidebar.selectbox("Select Classifier", ("SVM", "Logistic Regression", "Random Forest"))

# Initialize classifier
if classifier_option == "SVM":
    model = SVC(probability=True)
elif classifier_option == "Logistic Regression":
    model = LogisticRegression()
else:
    model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Display the evaluation metrics
st.write(f"Confusion Matrix for {classifier_option}")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Confusion Matrix")
st.pyplot()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
st.write(f"ROC AUC for {classifier_option}: {roc_auc:.2f}")
plt.figure()
plt.plot(fpr, tpr, color="darkorange", lw=2, label="ROC curve (area = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic")
plt.legend(loc="lower right")
st.pyplot()

# Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_proba)
st.write(f"Precision-Recall Curve for {classifier_option}")
plt.figure()
plt.plot(recall, precision, color="blue", lw=2, label="Precision-Recall curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend(loc="lower left")
st.pyplot()
```

---

## Dockerfile

```dockerfile
# Use a lightweight Python image
FROM python:3-slim

# Keeps Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . /app

# Ensure Streamlit runs as non-root user
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Expose the Streamlit default port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py"]
```

---

## requirements.txt

```txt
pandas
streamlit
scikit-learn
matplotlib
seaborn
```