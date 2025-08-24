
terraform {
  required_version = ">= 1.5.0"
  # backend "s3" {
  #   bucket = "YOUR_TF_STATE_BUCKET"
  #   key    = "enterprise/dev/terraform.tfstate"
  #   region = "us-east-1"
  #   dynamodb_table = "YOUR_TF_LOCK_TABLE"
  # }
}
provider "aws" { region = var.region }
module "vpc" { source = "../../modules/vpc" region = var.region }
module "eks" { source = "../../modules/eks" region = var.region }
output "vpc_id" { value = module.vpc.vpc_id }
output "eks_cluster_name" { value = module.eks.eks_cluster_name }
