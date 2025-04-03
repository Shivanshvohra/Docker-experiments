import streamlit as st
import psycopg2

# Define Database URL
DATABASE_URL = "postgresql://admin:adminpassword@my_postgres:5432/mydb"

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)  # Using the DATABASE_URL directly
        return conn
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None

# Function to fetch data from PostgreSQL
def fetch_users():
    conn = get_db_connection()
    if not conn:
        return []
    
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            return cur.fetchall()

# Function to insert a new user
def insert_user(name, email):
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        return True
    except Exception as e:
        st.error(f"Error inserting user: {e}")
        return False

# Streamlit UI
st.title("📊 Streamlit App with PostgreSQL")

# Display Users
st.subheader("User Data")
if st.button("Refresh Data 🔄"):
    users = fetch_users()
    if users:
        st.table(users)
    else:
        st.warning("No users found or database error.")
else:
    users = fetch_users()
    if users:
        st.table(users)
    else:
        st.warning("No users found or database error.")

# User Input Form
st.subheader("➕ Add New User")
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add User")
    
    if submitted:
        if name and email:
            if insert_user(name, email):
                st.success("User added successfully!")
            else:
                st.error("Failed to add user.")
        else:
            st.error("Please provide both name and email.")