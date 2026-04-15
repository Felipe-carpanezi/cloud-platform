remote_state {
  backend = "s3"

  config = {
    bucket         = "terraform-state-felipe-2026"
    key            = "dev/vpc/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}

include {
  path = find_in_parent_folders()
}

terraform {
  source = "../../../terraform/modules/vpc"
}

inputs = {
  vpc_cidr = "10.0.0.0/16"
}