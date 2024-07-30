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
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Docker
- Kubernetes cluster (e.g., Minikube, GKE, EKS)
- k6 for load testing
- kubectl command-line tool
- Python 3.x
- Flask library
- ollama library (or any custom libraries required by your application)

## Setup

### Building the Docker Image
To build the Docker image, navigate to the directory containing your `Dockerfile` and run:
```sh
docker build -t shubham9624/ollama .
