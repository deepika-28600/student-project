
# Cloud & DevOps Enterprise Platform 🚀

A **hire-me, enterprise-grade** portfolio project demonstrating a realistic Cloud & DevOps platform:
- Microservices (FastAPI **api**, Python **worker**), **Nginx frontend**, **Postgres**, **Redis**
- **Docker** for local dev, **Kubernetes + Helm** for cluster deploy, **Kustomize** overlays
- **IaC**: Terraform (AWS VPC + EKS skeleton, env layout)
- **CI/CD**: GitHub Actions – build, test, scan (Trivy), push to GHCR, Helm deploy
- **Observability**: Prometheus + Grafana (metrics), Loki-ready logging layout
- **Load testing**: k6
- **Makefile**: common developer workflow

> No secrets included. Configure your own AWS creds and GitHub Actions secrets. Helm values reference GHCR images (`ghcr.io/<owner>/<repo>`).

## One-minute local demo
```bash
make compose-up
# Frontend: http://localhost:8080
# API docs: http://localhost:8000/docs
make compose-down
```

## Kubernetes (Kind/Minikube)
```bash
make k8s-build      # builds local images
make helm-install   # installs chart into 'platform' namespace
kubectl -n platform get svc
```

## CI/CD workflow
- `.github/workflows/pipeline.yml` runs: lint/test → Docker buildx → Trivy scan → push images → Helm deploy (if on `main`).
- Image tags use commit SHA for immutability.

## Terraform (AWS or LocalStack)
- `infra/terraform/modules`: `vpc`, `eks` (skeleton)
- `infra/terraform/envs/dev`: starting point. State backends commented to avoid accidental cost.
- You can point providers to **LocalStack** for zero-cost demo.

## Structure
```
api/                 FastAPI service (with /metrics)
worker/              Python worker emitting Prometheus metrics
frontend/            Nginx static site that proxies to /api
deploy/helm/         Combined Helm chart (api, worker, frontend, postgres, redis)
deploy/kustomize/    Base + overlays (dev, prod)
infra/terraform/     Modules + dev env for AWS
ops/                 Prometheus, Grafana, k6
.github/workflows/   CI/CD
Makefile, docker-compose.yml, .gitignore
```

## Interview talking points
- **Shift-left security**: Trivy in CI; immutable tags; least-privileged k8s manifests (readiness/liveness, resources).
- **Scalability**: HPA-ready chart; separate stateless services; Redis as broker; Postgres as DB.
- **Reliability**: probes, rolling updates via Helm; dedicated namespace; can add ArgoCD for GitOps.
- **Observability**: Prometheus/Grafana; custom metrics; k6 baseline perf profile.
- **Cost-aware**: Local dev via Compose; Terraform skeleton avoids accidental spend; LocalStack-ready notes.
