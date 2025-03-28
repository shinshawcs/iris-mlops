# iris-mlops
# 🧠 Iris MLOps Project

This project demonstrates a complete machine learning pipeline using:

- **FastAPI** for inference API
- **Docker & Docker Compose** for containerization
- **MLflow** for experiment tracking
- **PostgreSQL** for logging prediction data
- **Kubernetes** (Minikube) for deployment
- **GitHub Actions** for CI/CD (auto deploy & test)

---

## 📁 Project Structure
.
├── app/                  # FastAPI + training logic
├── mlruns/               # MLflow tracking logs
├── k8s/                  # Kubernetes deployment files
├── .env                  # DB credentials
├── requirements.txt      # Python dependencies
├── Dockerfile            # FastAPI container
├── docker-compose.yml    # Compose setup for API + DB + MLflow
├── Makefile              # One-click commands
└── README.md

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/yourname/iris-mlops
cd iris-mlops

make up         # Build and start services
make train      # Train and log model to MLflow
make mlflow-ui  # Open MLflow tracking dashboard

FastAPI: http://localhost:8000/docs
MLflow UI: http://localhost:5001

Kubernetes Deployment (Minikube)
make k8s-deploy
kubectl port-forward service/iris-api-service 30080:80

GitHub Actions (CI/CD)
•	Auto format check
•	Build on push
•	Optionally push image to Docker Hub
•	Auto test training pipeline

Created by Xin Xiao
Machine Learning Engineer Track