📝 TaskFlow: A Production-Ready To-Do Application
TaskFlow is a full-stack Task Management application built with Django, designed to demonstrate a modern software development lifecycle. This project isn't just about the code—it’s about the infrastructure, utilizing Docker for containerization, Jenkins for CI/CD automation, and AWS for cloud deployment.
![Image Name](https://github.com/Jalil-hamdard/django-todo-jenkins/blob/main/Screenshot%202026-02-25%20093652.png?raw=true)

🚀 Features
CRUD Functionality: Add, toggle, and delete tasks in real-time.

Modern UI: A clean, responsive interface built with CSS Flexbox.

Containerized Architecture: Fully Dockerized for environment consistency.

Automated Pipeline: Integrated CI/CD via Jenkins.

Cloud Hosted: Deployed on an AWS EC2 instance.

🛠️ Tech Stack & Infrastructure
Backend & Frontend
Framework: Django 5.x (Python)

Database: SQLite (Development) / PostgreSQL (Production ready)

Styling: Custom CSS3 with a focus on UX/UI.

DevOps & Cloud
Containerization: Docker & Docker Compose used to package the Django app, ensuring it runs the same on my machine as it does on the server.

CI/CD Pipeline: Jenkins automates the workflow. On every push to the main branch, Jenkins:

Pulls the latest code.

Builds the Docker image.

Runs tests (if applicable).

Pushes the image to a registry or deploys directly.

Cloud Provider: AWS (Amazon Web Services).

EC2 (Elastic Compute Cloud): Hosts the live application within a Linux environment.

Security Groups: Configured for HTTP (8000/80) access.

📦 Local Setup
If you want to run this project locally using Docker:

Clone the repository:

Build and Run with Docker:

Access the app:
Open your browser and go to http://localhost:8000

🏗️ Deployment Architecture
The workflow follows a standard industry pipeline:

Develop: Code changes are made locally.

Commit: Code is pushed to GitHub.

Trigger: Jenkins detects the push via Webhooks.

Deploy: Jenkins executes a shell script on the AWS EC2 instance to pull the latest Docker image and restart the containers.
