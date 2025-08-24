
# VPC module (skeleton)
terraform { required_version = ">= 1.5.0" }
provider "aws" { region = var.region }
resource "aws_vpc" "main" { cidr_block = "10.0.0.0/16" }
output "vpc_id" { value = aws_vpc.main.id }
