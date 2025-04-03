FROM python:3.11

WORKDIR /code

# Install dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements and install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copy application files
COPY stream.py /code/

CMD ["python", "stream.py"]
