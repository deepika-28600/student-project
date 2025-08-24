
terraform { required_version = ">= 1.5.0" }
provider "aws" { region = var.region }
# EKS skeleton module (placeholder for cluster + node groups)
output "eks_cluster_name" { value = "enterprise-eks" }
