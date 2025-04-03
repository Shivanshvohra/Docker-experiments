# Streamlit App with PostgreSQL using Docker

This project demonstrates how to set up a Streamlit application that connects to a PostgreSQL database using Docker. The setup involves creating a custom Docker network, running a PostgreSQL container, inserting dummy data, and deploying a Streamlit container that fetches data from the database.

## Prerequisites
- Docker installed on your system
- Basic knowledge of Docker, PostgreSQL, and Python

## Setup Instructions

### Step 1: Create a Custom Docker Network
```sh
docker network create --driver bridge my_custom_network
```
This ensures communication between the PostgreSQL and Streamlit containers.

### Step 2: Run PostgreSQL Container
```sh
docker run -d \
  --name my_postgres \
  --network my_custom_network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=adminpassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres
```
This starts a PostgreSQL container with:
- Username: `admin`
- Password: `adminpassword`
- Database: `mydb`
- Exposes port `5432` for local access

### Step 3: Insert Dummy Data
#### Connect to PostgreSQL CLI
```sh
docker exec -it my_postgres psql -U admin -d mydb
```
#### Create Table and Insert Data
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com');

SELECT * FROM users;
```
#### Exit PostgreSQL
Type `\q` and press Enter.

### Step 4: Create Streamlit App
Create a `stream.py` file with the following content:
```python
import streamlit as st
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydb",
        user="admin",
        password="adminpassword",
        host="my_postgres",  # PostgreSQL container name as hostname
        port="5432"
    )
    return conn

st.title("Streamlit App with PostgreSQL")

try:
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    st.write("### User Data from PostgreSQL")
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    
    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error connecting to database: {e}")
```

### Step 5: Create Dockerfile for Streamlit
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir streamlit psycopg2
EXPOSE 8501
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 6: Build and Run the Streamlit Container
#### Build the Image
```sh
docker build -t my_streamlit_app .
```
#### Run the Container
```sh
docker run -d \
  --name streamlit_app \
  --network my_custom_network \
  -p 8501:8501 \
  my_streamlit_app
```

### Step 7: Test the Setup
- Open a browser and visit: [http://localhost:8501](http://localhost:8501)
- You should see user data fetched from the PostgreSQL database.

## Summary
✅ Created a custom Docker network (`my_custom_network`)

✅ Launched a PostgreSQL container and inserted dummy data

✅ Created a Streamlit app that connects to the database

✅ Built and ran the Streamlit container on the same network

✅ Opened `http://localhost:8501` to view the app

## Cleanup
To stop and remove the containers:
```sh
docker stop my_postgres streamlit_app
docker rm my_postgres streamlit_app
docker network rm my_custom_network
```

## License
This project is open-source and free to use.
