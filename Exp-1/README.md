# EXP-1: Streamlit Spiral Visualization App with Docker

Welcome to the *Streamlit Spiral Visualization App*! This project demonstrates a simple and interactive Python application built with *Streamlit* to visualize a spiral. You can customize the spiral’s characteristics using adjustable sliders and view the changes in real-time. The app is Dockerized for easy deployment and consistency across environments.

## 🌟 Features
- **Interactive Controls:** Use sliders to adjust the number of points and turns in the spiral.
- **Dynamic Visualization:** Watch the spiral change dynamically in response to slider adjustments.
- **Dockerized Application:** The app is packaged within a Docker container, ensuring portability and easy deployment.

## 🚀 Technologies Used
- **Python 3:** The core programming language for this app.
- **Streamlit:** A framework for building interactive and beautiful web applications.
- **Altair:** A declarative statistical visualization library for Python used for rendering the spiral.
- **Docker:** Containerizes the app for consistent behavior across different environments.
- **Pandas:** Used for data manipulation and handling data frames.

## ⚙ Prerequisites
Before running the application, ensure you have the following installed on your local machine:

- **Docker:** To build and run the app inside a container.
- **Git:** To clone the repository.

If you don't have Docker installed, follow the instructions in the [official Docker Installation Guide](https://docs.docker.com/get-docker/).

## 🛠 Getting Started
Follow these steps to set up and run the application either locally or inside a Docker container:

### Step 1: Clone the Repository
Clone the repository to your local machine by running:

```sh
git clone https://github.com/BhavyaDhimxn/container-experiments.git
cd container-experiments
```

### Step 2: Create a `requirements.txt` File
Ensure the project directory includes a `requirements.txt` file containing the necessary dependencies:

```txt
streamlit
altair
pandas
```

### Step 3: Build the Docker Image
Build the Docker image from the project directory:

```sh
docker build -t streamlit .
```

This will use the `Dockerfile` to build the image named `streamlit`.

#### Check If the Image is Built
After building the image, you can check if it has been created by either:

- **Using Docker Desktop:** Go to the **Images** section to verify if the `streamlit` image is listed.
- **Using the Command Line:** Run the following command to list all Docker images:

```sh
docker images
```

This command will display all available images, including the `streamlit` image if it has been successfully built.

### Step 4: Run the Docker Container
Start the app inside a Docker container by running:

```sh
docker run -p 8501:8501 streamlit
```

This command will map port `8501` inside the container to port `8501` on your local machine.

### Step 5: Access the Streamlit App
After running the container, open your browser and go to:

[http://localhost:8501](http://localhost:8501)

The Streamlit app should now be visible, allowing you to interactively adjust the spiral’s number of points and turns.

## 🌀 How the App Works
### Sliders for Customization
- **Number of points in spiral:** Controls the number of points that form the spiral.
- **Number of turns in spiral:** Adjusts how many full turns the spiral makes.

### Real-Time Visualization
As you adjust the sliders, the spiral is dynamically updated in real-time.

### Under the Hood
The app generates the spiral points based on polar coordinates. The `x` and `y` positions are calculated using mathematical functions, and the results are rendered using Altair charts in the Streamlit app.

## 💻 Code Explanation
### Streamlit Python Code for Spiral Visualization
```python
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from collections import namedtuple

# Define a namedtuple to store points in the spiral
Point = namedtuple('Point', ['x', 'y'])

# Function to generate the spiral data
def generate_spiral(num_points, num_turns):
    data = []
    for i in range(num_points):
        angle = 2 * np.pi * num_turns * (i / num_points)
        radius = i / num_points
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        data.append(Point(x, y))
    return data

# Streamlit App Layout
st.title("Interactive Spiral Visualization")

# Sliders for user input
num_points = st.slider('Number of Points in Spiral', min_value=50, max_value=1000, value=500)
num_turns = st.slider('Number of Turns in Spiral', min_value=1, max_value=10, value=5)

# Generate the spiral data
spiral_data = generate_spiral(num_points, num_turns)

# Convert the spiral data to a DataFrame for visualization
spiral_df = pd.DataFrame(spiral_data, columns=['x', 'y'])

# Create the Altair chart to visualize the spiral
chart = alt.Chart(spiral_df).mark_circle(size=3).encode(
    x='x',
    y='y'
).properties(
    width=600,
    height=600
)

# Display the chart
st.altair_chart(chart, use_container_width=True)
```

### `Dockerfile`
```dockerfile
# Use official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
```

### `requirements.txt`
```txt
streamlit
altair
pandas
```

## 🛠 Troubleshooting
If you encounter any issues, here are a few tips:

- **Check Docker Logs:** If the container fails to start, use the following command to check the logs:
  
  ```sh
  docker logs <container_id>
  ```

- **Ensure Dependencies are Installed:** If there are errors related to missing packages, make sure the `requirements.txt` is correctly copied into the Docker image, and the `pip install` command runs successfully during the Docker build.

## 🤝 Contributing
We welcome contributions to improve this project! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request to merge your changes into the main repository.

**Happy Coding! 🎉**
