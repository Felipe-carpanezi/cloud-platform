terraform {
  source = "../../../terraform/modules/eks"
}

include {
  path = find_in_parent_folders()
}

dependency "vpc" {
  config_path = "../vpc"
}

inputs = {
  vpc_id     = dependency.vpc.outputs.vpc_id
  subnet_ids = dependency.vpc.outputs.public_subnets

  admin_arn = "arn:aws:iam::589234081834:user/terraform-user"
}