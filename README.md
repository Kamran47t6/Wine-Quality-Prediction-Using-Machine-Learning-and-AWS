# Wine Prediction Machine Learning

Wine Prediction ML is an end-to-end Machine Learning application built using modern MLOps practices to predict wine quality from user-provided features.

The project integrates modular ML pipelines, configuration-driven experimentation, Docker containerization, CI/CD automation, and cloud deployment using AWS EC2 and Amazon ECR to demonstrate real-world production deployment workflows.

---

## 📌 Features

### 🍇 Wine Quality Prediction
Predict wine quality instantly through a simple web interface.

### ⚙️ End-to-End ML Pipeline
Implements complete ML lifecycle from data ingestion to model evaluation.

### 📁 Config-Driven Architecture
Uses YAML configuration files to enable reproducible experiments.

### 🐳 Docker Containerization
Ensures consistent runtime environment across development and deployment.

### 🔁 CI/CD Automation
Automatically builds and deploys application using GitHub Actions.

### ☁️ AWS Cloud Deployment
Deploys Docker images from Amazon ECR to AWS EC2 instances.

### 🌐 Interactive Web Interface
Provides a responsive HTML interface for user input and prediction output.

---

## 🧠 Tech Stack

| Layer | Technology |
|------|-----------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Web Framework | Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud Platform | AWS EC2 |
| Container Registry | AWS ECR |
| Configuration | YAML |
| Frontend | HTML, CSS |

---

## Prerequisites

Ensure required tools are installed before running the project locally.

- Python 3.12+
- Git
- Docker (optional but recommended)
- AWS CLI configured (for cloud deployment)

Install dependencies:

```bash
pip install -r requirements.txt
---

## Project Structure

Wine_Prediction_ML/
│
├── .github/workflows/
│   └── cicd.yaml
│
├── artifacts/
├── config/
├── logs/
├── research/
│
├── src/Wine_Prediction_ML/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── pipeline/
│   └── utils/
│
├── static/
├── templates/
│   └── index.html
│
├── app.py
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
├── Dockerfile
└── setup.py

---

## Setup Instructions

Clone Repository

```bash
git clone https://github.com/yourusername/Wine_Prediction_ML.git
```
```bash
cd Wine_Prediction_ML
```
```bash
conda create -n mlproject python=3.12 -y
```
```bash
conda activate mlproject 
```

```bash
pip install -r requirements.txt 
```

```bash
python app.py
```

```bash
Now Open the Local Host 0.0.0.0:8080
```
---

## Docker Deployment

Run the application inside a container for production consistency.

Build Docker Image
under Dockerfile

---

## AWS Deployment Workflow

This project supports automated deployment on AWS cloud infrastructure.

Amazon ECR

Docker images are pushed to Amazon Elastic Container Registry.

AWS EC2

GitHub Actions pulls the image from ECR and runs container on EC2 instance.

This enables fully automated cloud deployment pipeline.

---

## CI/CD Workflow

Continuous Integration and Deployment is configured using GitHub Actions.

On every push:

Docker image is built

Image is pushed to Amazon ECR

Existing container is stopped

```bash
docker rm -f cnncls || true
```

New container is deployed on AWS EC2

⚡ How It Works

The system processes user input through trained ML models to generate predictions.

### Frontend

User enters wine feature values via HTML interface.

### Backend

Application loads trained model and processes input request.

### Prediction

ML model predicts wine quality based on trained patterns.

### Response

Prediction result is displayed instantly on UI.

----

## Key Components

Core modules responsible for pipeline execution and prediction workflow.

### Components Layer

Implements individual ML stages such as ingestion and training.

### Pipeline Layer

Controls execution order and dependency between stages.

### Entity Layer

Defines structured configuration objects.

### Utils Layer

Provides reusable helper functions across modules.

---

## Development Workflow

Guidelines for extending or modifying project functionality.

Update UI in templates/index.html

Modify pipeline logic in src/components

Tune hyperparameters in params.yaml

Update deployment logic in .github/workflows
