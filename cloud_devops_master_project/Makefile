
SHELL := /bin/bash

compose-up:
	docker compose up -d --build

compose-down:
	docker compose down -v

k8s-build:
	docker build -t api:local ./api
	docker build -t worker:local ./worker
	docker build -t frontend:local ./frontend

k8s-helm-install:
	namespace=platform; kubectl get ns $$namespace >/dev/null 2>&1 || kubectl create ns $$namespace; 	helm upgrade --install platform ./deploy/helm -n $$namespace

k8s-helm-uninstall:
	helm uninstall platform -n platform || true
