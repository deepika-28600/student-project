
terraform {
  required_version = ">= 1.5.0"
}
provider "aws" {
  region  = var.region
  # For local demo, consider LocalStack: set endpoint overrides via provider config or env
}
module "vpc" {
  source = "../../modules/vpc"
  region = var.region
}
module "eks" {
  source = "../../modules/eks"
  region = var.region
}
output "vpc_id" { value = module.vpc.vpc_id }
output "eks_cluster_name" { value = module.eks.eks_cluster_name }
