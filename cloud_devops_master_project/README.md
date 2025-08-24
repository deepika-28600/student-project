
# Cloud & DevOps Master Project — Microservices, IaC, CI/CD, Observability

A production-style portfolio project demonstrating:
- **Microservices** (FastAPI `api`, Celery `worker`, Nginx `frontend`)
- **Containerization** with Docker
- **Kubernetes** (Helm chart) for deployment
- **Infrastructure as Code** with Terraform (AWS, modular layout)
- **CI/CD** with GitHub Actions (build, test, scan, publish to GHCR, deploy)
- **Observability** with Prometheus + Grafana
- **Load testing** with k6
- **Makefile** for common tasks

> Note: Secrets/tokens are **not** included. Use GitHub Actions secrets and your own cloud credentials. Terraform is structured for AWS; you can also point it to **LocalStack** for local demo.

## Quick Start (Local - Docker Compose)
```bash
make compose-up
# Visit: http://localhost:8080  (frontend)
# API:    http://localhost:8000/docs
make compose-down
```

## Kubernetes (Kind/Minikube demo)
```bash
# Build images locally
make k8s-build
# Install via Helm
make k8s-helm-install
# Port forward
kubectl -n platform port-forward svc/frontend 8080:80 &
kubectl -n platform port-forward svc/api 8000:80 &
```

## CI/CD
- Workflow: `.github/workflows/ci-cd.yml`
- Jobs: lint/test → build → Trivy scan → push to GHCR → Helm deploy (if main).

## Terraform (AWS/LocalStack)
- Modules for VPC + EKS (skeleton). Apply with your credentials or set `TF_VAR_use_localstack=true` for LocalStack demos.

## Observability
- Prometheus scrapes `api` and `worker` metrics.
- Grafana with a starter dashboard provisioned.

## Structure
```
api/              # FastAPI microservice
worker/           # Celery worker (Redis broker)
frontend/         # Nginx static site
deploy/helm/      # Helm chart
deploy/k8s/       # Raw k8s manifests
infra/terraform/  # Terraform modules & envs
ops/              # Observability, k6 tests
.github/workflows # CI/CD
Makefile
docker-compose.yml
```

---

### Talking Points for Interviews
- Explain **why Helm** (templating, values per env), **why GHCR** (immutable images), **shift-left security** (Trivy in CI), **GitOps-friendly** structure, **observability SLOs** (latency, error rate).
- Discuss blue/green/rolling strategies (Helm `strategy`), HPA on CPU/requests (placeholder manifests).
- Show Terraform plan/apply and state management (S3 + DynamoDB — commented defaults to avoid costs).

