
# EKS module (skeleton)
terraform { required_version = ">= 1.5.0" }
provider "aws" { region = var.region }
# Normally EKS cluster resources would go here
output "eks_cluster_name" { value = "demo-eks" }
