
SHELL := /bin/bash

compose-up:
	docker compose up -d --build

compose-down:
	docker compose down -v

k8s-build:
	docker build -t api:local ./api
	docker build -t worker:local ./worker
	docker build -t frontend:local ./frontend

helm-install:
	ns=platform; kubectl get ns $$ns >/dev/null 2>&1 || kubectl create ns $$ns; 	helm upgrade --install platform ./deploy/helm -n $$ns

helm-uninstall:
	helm uninstall platform -n platform || true
