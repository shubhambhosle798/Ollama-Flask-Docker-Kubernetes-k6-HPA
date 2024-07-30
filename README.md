# Ollama-Flask-Docker-Kubernetes-k6-HPA

## Overview
This project provides a text generation API using Flask, Docker, and Kubernetes. The application includes load testing with k6 and autoscaling using Kubernetes HPA (Horizontal Pod Autoscaler).

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Building the Docker Image](#building-the-docker-image)
  - [Deploying to Kubernetes](#deploying-to-kubernetes)
  - [Setting Up HPA](#setting-up-hpa)
- [API Endpoints](#api-endpoints)
- [Testing Methodology](#testing-methodology)
  - [Load Testing](#load-testing)
  - [Results](#results)
- [Autoscaling](#autoscaling)
- [Troubleshooting](#troubleshooting)

## Prerequisites
- Docker
- Minikube Kubernetes cluster
- k6 for load testing
- Python
- Flask library
- ollama library

## Setup

### Building the Docker Image
To build the Docker image, navigate to the directory containing your `Dockerfile` and run:
```sh
docker build -t shubham9624/ollama .
```

### Deploying to Kubernetes
To deploy the application to your Kubernetes Minikube cluster, use the provided YAML configuration files:
```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

### Setting Up HPA
Configure the Horizontal Pod Autoscaler using the provided HPA YAML file:
```sh
kubectl apply -f hpa.yaml
```

### API Endpoints
#### GET /
- Returns a welcome message.
- URL: http://<external-ip>:30002/
- Response: 'Welcome to the Ollama Text Generation API'

#### POST /generate
- Generates text based on a provided prompt.
- URL: http://<external-ip>:30002/generate
- Request Body:
```sh
  {
  "prompt": "Test prompt"
  }
```
- Response:
```
  {
  "response": "Generated text based on the prompt"
  }
```
### Testing Methodology
#### Load Testing
Load testing was performed using k6 to simulate user traffic and measure the API's performance under stress.

#### Results
Results Summary:

### Autoscaling
The application uses Kubernetes HPA to automatically scale the number of replicas based on CPU utilization.

### Troubleshooting
#### Common Issues
- Port conflicts
- Service not accessible
- Autoscaling not working as expected

#### Solutions
- Ensure no other application is using the specified ports.
- Verify Kubernetes service and pod logs.
- Check HPA metrics and ensure they align with the expected resource usage.



### Contributions are welcome! Thankyou :)
