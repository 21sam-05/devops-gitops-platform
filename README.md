# GitOps-Based Microservices Platform

A production-oriented DevOps project demonstrating containerization,
CI/CD, GitOps, Kubernetes, infrastructure as code, monitoring,
and automated deployment.

## Current Architecture

The application currently consists of two FastAPI microservices:

- Task Service
- Notification Service

Both services run as Docker containers and communicate through
a Docker network managed by Docker Compose.

## Current Stack

- Python
- FastAPI
- Docker
- Docker Compose
- Pytest
- Git

## Current Features

- Containerized microservices
- Service-to-service HTTP communication
- Docker Compose orchestration
- Health endpoints
- Automated tests

## Planned Architecture

The project will eventually include:

- GitHub Actions
- Container registry
- Kubernetes
- Helm
- Argo CD
- Prometheus
- Grafana
- Horizontal Pod Autoscaling
- Terraform
- AWS EKS

## Project Goal

Build and document a complete GitOps-based CI/CD platform
while learning each component through practical implementation.