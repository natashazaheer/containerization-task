# Containerization and Orchestration Assignment

This project demonstrates how to containerize a Flask application using **Docker** and orchestrate multiple services using **Docker Compose**. The setup includes a Flask web application, a Redis cache, and a PostgreSQL database.

---

## Project Structure

- **docker/** → Contains the Flask application script, Dockerfile, and requirements file.  
- **docker-compose/** → Contains the Docker Compose configuration for orchestrating services.  

---

##Steps Performed

### Step 1: Docker Setup
- Installed Docker Desktop on the local machine and verified installation with `docker --version`.  
- Created a simple Python Flask application that displays a styled HTML page with name and status details.  
- Added a `requirements.txt` file listing necessary dependencies like Flask and Gunicorn.  
- Wrote a `Dockerfile` in the `docker/` directory to containerize the application.  
- Built the Docker image using the build command.  
- Ran the container locally, mapping port 5000 on the container to the host machine for browser access.  
- Verified the application was accessible at [http://localhost:5000](http://localhost:5000).  
- Logged in to Docker Hub and pushed the image to the registry for storage and reuse.  

---

### Step 2: Docker Compose Setup
- Created a `docker-compose.yml` file to simplify running services.  
- Defined a web service for the Flask application using the Dockerfile created earlier.  
- Started services using the Docker Compose command.  
- Added a second service, a lightweight Redis cache, to meet the multi-service requirement and enable simple connectivity testing.  
- Confirmed both services were running with `docker ps`.  
- Verified that the Flask app could communicate with Redis using the internal hostname `cache`.  

---

### Step 3: Adding Database Service
- Modified the `docker-compose.yml` file to include a PostgreSQL database service named `db`.  
- Configured environment variables in the Compose file for the database name, username, and password.  
- Launched the updated setup with Docker Compose to run Flask, Redis, and PostgreSQL simultaneously.  
- Accessed the PostgreSQL CLI to confirm the database was operational and ready for queries.  

---

### Step 4: Verification
- Used `docker ps` to verify all three services — **Flask, Redis, and PostgreSQL** — were running together.  

---

## Key Outcomes
- Successfully containerized a Flask application using Docker.  
- Implemented multi-service orchestration with Docker Compose.  
- Verified inter-service connectivity between the application, Redis cache, and PostgreSQL database using defined service names in the Compose network.  

