# Use an official Python runtime as a parent image
FROM python:3.12.0

# Install system dependencies and ODBC Driver 17 for SQL Server
RUN apt-get update && apt-get install -y tzdata\
    curl \
    gnupg2 \
    apt-transport-https \
    unixodbc \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list -o /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && rm -rf /var/lib/apt/lists/*

#Set the timezone
ENV TZ=Africa/Dar_es_Salaam

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

RUN mkdir -p logs && touch logs/app.log

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8888

# Define environment variable
ENV PYTHONPATH=/app

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]
