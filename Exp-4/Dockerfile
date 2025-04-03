# Use Python as base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir streamlit psycopg2

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]